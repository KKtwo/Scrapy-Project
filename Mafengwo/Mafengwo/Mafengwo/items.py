# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MafengwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # page_urls = scrapy.Field()
    userID = scrapy.Field()    #用户ID
    image_urls = scrapy.Field()
    articleID = scrapy.Field()
    # image_id = scrapy.Field()
    #image_path = scrapy.Field()


