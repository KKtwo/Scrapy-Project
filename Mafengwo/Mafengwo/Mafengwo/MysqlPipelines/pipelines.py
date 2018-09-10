# -*- coding: utf-8 -*-
from Mafengwo.items import MafengwoItem
from Mafengwo.spiders import MafengwoSpider
import pymongo
from pymongo.errors import DuplicateKeyError
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
mongo = pymongo.MongoClient('127.0.0.1',27017)


class MafengwoPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, MafengwoItem):
            try:
                mongo["mafengwo"]["All"].insert({'_id':item['articleID'],'userID':item['userID'],
                                                       'imgs_urls':item['image_urls']})
                print("存入成功！articleID:%s inserted"%item['articleID'])
                return item
            except DuplicateKeyError as err:
                print(err)
                print('主键重复，不存入')

            try:
                mongo["mafengwo"]["VisitedFiji"].insert({'_id': item['page_urls']})

            except DuplicateKeyError as err:
                print(err)
                print('主键重复，不存入页面url')
        return item

class NumberCheck(object):
    @classmethod
    def find_remain_pages(cls,all_page): #去重
        myMongo=mongo["mafengwo"]["VisitedFiji"].find()
        alist = []
        for o in myMongo:
            alist.append(o['_id'])
        print(alist)
        #cursor.execute(sql)
        #result=cursor.fetchall()  #fetchall返回所有数据列表
        remain_page = list(set(all_page).difference(alist))
        print(remain_page)
        return remain_page

