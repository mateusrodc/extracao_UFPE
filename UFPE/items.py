# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UfpeItem(scrapy.Item):
    title = scrapy.Field()
    authors = scrapy.Field()
    keywords = scrapy.Field()
    abstract = scrapy.Field()
    uri = scrapy.Field()
