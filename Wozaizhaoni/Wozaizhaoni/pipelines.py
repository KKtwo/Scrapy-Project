# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from Wozaizhaoni.items import WozaizhaoniItem

import os

class WozaizhaoniPipeline(ImagesPipeline):
    headers = {
        # 'Host': 'jp.match.com',
        # 'Connection': 'keep-alive',
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'ADRUM': 'isAjax:true',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
        # 'Accept': '*/*',
        # 'Referer': 'https://jp.match.com/search?lid=2&st=Q',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    def get_media_requests(self,item,info): 
        for url in item['image_url']:
            yield scrapy.Request(url,headers=self.headers,meta={'item':item})
    def file_path(self,request,response=None,info=None):
        item=request.meta['item'] 
        filename = u'/{0}/{1}'.format(item['user_id'], request.url[38:]) 
        return filename
