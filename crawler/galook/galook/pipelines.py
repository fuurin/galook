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
        self.conn.close()

    def process_item(self, item, spider):
        # editions テーブル
        sql = textwrap.dedent("""\
        INSERT INTO editions (id, title, brand, price, release_date, story, url) \
        VALUES (%s, %s, %s, %s, %s, %s, %s);\
        """)
        curs = self.conn.cursor()
        curs.execute(
            sql, (
                item['id'], item['title'], item['brand'], item['price'], 
                item['release_date'], item['story'], item['url']
            )
        )

        # categories テーブル
        for category in item['category']:
            sql = textwrap.dedent("""\
            INSERT INTO categories (edition_id, category_name) \
            VALUES (%s, %s);\
            """)
            curs = self.conn.cursor()
            curs.execute(sql, (item['id'], category))

        # subgenres テーブル
        for subgenre in item['subgenre']:
            sql = textwrap.dedent("""\
            INSERT INTO subgenres (edition_id, subgenre_name) \
            VALUES (%s, %s);\
            """)
            curs = self.conn.cursor()
            curs.execute(sql, (item['id'], subgenre))

        # # writers テーブル
        for writer in item['writer']:
            sql = textwrap.dedent("""\
            INSERT INTO writers (edition_id, writer_name) \
            VALUES (%s, %s);\
            """)
            curs = self.conn.cursor()
            curs.execute(sql, (item['id'], writer))

        self.conn.commit()

        return item
