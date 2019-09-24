# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import textwrap
from urllib.parse import urlparse
import scrapy
import psycopg2


class PostgresPipeline(object):
    def open_spider(self, spider: scrapy.Spider):
        url = os.getenv('GALOOK_DATABASE_URL')
        parsed_url = urlparse(url)
        username = parsed_url.username
        database = parsed_url.path[1:]
        hostname = parsed_url.hostname
        self.conn = psycopg2.connect(
            database = database, 
            user = username,
            host = hostname
        )

    def close_spider(self, spider: scrapy.Spider):
        pass

    def execute_sql(self, sql, args):
        try:
            curs = self.conn.cursor()
            curs.execute(sql, args)
        except psycopg2.errors.InFailedSqlTransaction as e:
            print(e)
            print(sql)
        return curs

    def exists(self, curs):
        if curs.description is None:
            return False
        return curs.fetchone()[0]

    def is_new_standard(self, item, standard_price, standard_id):
        return (item['price'] != -1 and item['price'] < standard_price) or (item['price'] == standard_price and item['id'] < standard_id)

    def process_item(self, item, spider):
        # 存在判定
        curs = self.execute_sql("SELECT EXISTS(SELECT id FROM editions WHERE id = %s);", (item['id'], ))
        if self.exists(curs):
            return item
        # editions テーブル
        curs = self.execute_sql(
            textwrap.dedent("""\
            INSERT INTO editions (id, title, brand, price, release_date, story, url) \
            VALUES (%s, %s, %s, %s, %s, %s, %s);\
            """), (
                item['id'], item['title'], item['brand'], item['price'], 
                item['release_date'], item['story'], item['url']
            )
        )

        # # categories テーブル
        for category in item['category']:
            curs = self.execute_sql(
                textwrap.dedent("""\
                INSERT INTO categories (edition_id, category_name) \
                VALUES (%s, %s);\
                """), 
                (item['id'], category)
            )

        # # subgenres テーブル
        for subgenre in item['subgenre']:
            curs = self.execute_sql(
                textwrap.dedent("""\
                INSERT INTO subgenres (edition_id, subgenre_name) \
                VALUES (%s, %s);\
                """), 
                (item['id'], subgenre)
            )

        # # writers テーブル
        for writer in item['writer']:
            curs = self.execute_sql(
                textwrap.dedent("""\
                INSERT INTO writers (edition_id, writer_name) \
                VALUES (%s, %s);\
                """), 
                (item['id'], writer)
            )

        # games テーブル・editions テーブルの game_id 列
        standard_id = None
        if item['story']:
            curs = self.execute_sql("SELECT EXISTS(SELECT id FROM games WHERE story = %s);", (item['story'], ))
            if self.exists(curs):
                curs = self.execute_sql(
                    textwrap.dedent("""\
                    SELECT id, standard_edition_id FROM games WHERE story = %s;
                    """), 
                    (item['story'], )
                )
                game_id, standard_id = curs.fetchone()
        if not standard_id:
            curs = self.execute_sql(
                textwrap.dedent("""\
                INSERT INTO games (title, brand, story, standard_edition_id) \
                VALUES (%s, %s, %s, %s);\
                """), (
                    item['title'], item['brand'], item['story'], item['id']
                )
            )

            curs = self.execute_sql(
                textwrap.dedent("""\
                UPDATE editions \
                SET game_id = (SELECT MAX(id) FROM games)\
                WHERE id = %s;
                """), 
                (item['id'], )
            )
        else:
            curs = self.execute_sql(
                textwrap.dedent("""\
                UPDATE editions \
                SET game_id = %s\
                WHERE id = %s;
                """), 
                (game_id, item['id'])
            )
            curs = self.execute_sql(
                "SELECT price FROM editions WHERE id = %s;", 
                (standard_id, )
            )
            standard_price = curs.fetchone()[0]
            if self.is_new_standard(item, standard_price, standard_id):
                curs = self.execute_sql(
                    textwrap.dedent("""\
                    UPDATE games \
                    SET standard_edition_id = %s\
                    WHERE standard_edition_id = %s;
                    """), 
                    (item['id'], standard_id)
                )
        
        self.conn.commit()

        return item
