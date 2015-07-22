# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()



class DbbookItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    book = scrapy.Field()
    author = scrapy.Field()
    author_link = scrapy.Field()
    book_link = scrapy.Field()


