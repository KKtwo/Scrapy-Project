# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    
    image_url = scrapy.Field()
    age = scrapy.Field()
    user_id = scrapy.Field()

# ['青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県','新潟県','富山県','石川県','福井県','山梨県','長野県','岐阜県','静岡県','愛知県','三重県','滋賀県','京都府','兵庫県','奈良県','和歌山県','鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県',]
# [52,17,25,2,48,9,15,41,11,36,4,54,20,30,46,16,7,50,27,10,39,1,24,37,23,14,29,51,45,38,32,12,49,43,18,5,21,8,35,28,22,31,26,19,33]