# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os
# import re
import random
class NanspiderPipeline(ImagesPipeline):
    # pat = re.compile('wK\S+')
    def get_media_requests(self,item,info): 
        for url in item['image_url']:
            yield scrapy.Request(url,meta={'item':item})
    def file_path(self,request,response=None,info=None):
        item=request.meta['item'] 
        # m = self.pat.search(request.url)
        filename = u'/{0}/{1}'.format(item['user_id'],request.url[-7:]+'.jpg') 
        return filename
