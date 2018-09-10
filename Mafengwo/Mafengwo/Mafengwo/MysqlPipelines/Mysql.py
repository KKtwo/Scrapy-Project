# -*-coding:utf-8 -*-
from Mafengwo import settings
import mysql.connector
import pymongo
from pymongo.errors import DuplicateKeyError

'''db=mysql.connector.Connect(host='localhost', user='root', password='Jack@1997', port=3306, database='Mafengwo')

cursor=db.cursor()

print(u'成功连接数据库！')

class MySql(object):
    @classmethod
    def insert_data(cls, item):
        sql = "INSERT INTO users(userID) VALUES(%s)"
        values = (item['userID'])
        cursor.execute(sql, values)
        db.commit()

    @classmethod
    def insert_db(cls,item):
        image_id = item['image_id']
        image_url = item['image_urls']
        # print(image_id)
        # print(request.url)
        image_guid = "Australia" + "_" + image_id + "_" + image_url.split('/')[-1].split('?')[0]
        print(image_guid)
        path = item['image_id'] + '/%s' % (image_guid)
        sql="INSERT INTO test(userID,page_url,img_url,img_path) VALUES(%s,%s,%s,%s)"
        values=(item['userID'],item['page_url'],item['image_urls'], path)
        cursor.execute(sql,values)
        db.commit()

class NumberCheck(object):
    @classmethod
    def find_remain_pages(cls,all_page):
        sql="SELECT page_url FROM test"
        cursor.execute(sql)
        result=cursor.fetchall()  #fetchall返回所有数据列表
        remain_page = list(set(all_page).difference(result))
        return remain_page

    @classmethod
    def find_user(cls, userID):
        sql = "SELECT EXISTS(SELECT 1 FROM Australia WHERE userID=%(userID)s)"
        value = {
            'userID': userID
        }
        cursor.execute(sql, value)
        result = cursor.fetchall()
        for row in result:
            last_num = row[0]
            return last_num'''
