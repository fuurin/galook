# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Game(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    release_date = scrapy.Field()
    writer = scrapy.Field()
    subgenre = scrapy.Field()
    category = scrapy.Field()
    story = scrapy.Field()

