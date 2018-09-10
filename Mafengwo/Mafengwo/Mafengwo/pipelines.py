# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline

class MafengwocrawlerPipeline(ImagesPipeline):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'n1-q.mafengwo.net',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
    }
    def get_media_requests(self, item, info):
        # 处理对象:每组item中的每张图片
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        image_id = request.meta['item']['image_id']
        #print(image_id)
        #print(request.url)
        item = request.meta['item']
        image_guid = "Australia"+"_"+image_id+"_"+request.url.split('/')[-1].split('?')[0]
        #print(image_guid)
        path = item['image_id'] + '/%s' % (image_guid)
        print(path)
        return path

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        item['image_path'] = image_path
        return item
