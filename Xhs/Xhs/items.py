# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XhsItem(scrapy.Item):
    # define the fields for your item here like:
    
    image_url = scrapy.Field()
    user_id = scrapy.Field()
    t_id = scrapy.Field()