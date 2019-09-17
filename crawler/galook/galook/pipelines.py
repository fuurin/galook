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
        INSERT INTO editions (id, title, brand, price, release_date, url, story) \
        VALUES (%s, %s, %s, %s, %s, %s, %s);\
        """)
        curs = self.conn.cursor()
        curs.execute(
            sql, (
                item['id'], item['title'], item['brand'], item['price'], 
                item['release_date'], item['url'], item['story']
            )
        )

        # categories テーブル

        # subgenres テーブル

        # writers テーブル

        self.conn.commit()

        return item
