import json
import redis
import pymongo
# import pymysql

def save_to_mongodb():
    ''' 把redis数据库中的数据存入mongodb '''
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
    # 指定MongoDB数据库信息
    mongocli = pymongo.MongoClient(host='127.0.0.1',port=27017)

    # 创建数据库
    db = mongocli['match']
    # 创建表
    sheet = db['user']
    # 去重
    sheet.create_index('user_id', unique=True)
    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(['myspider:items'], timeout=3)
        item = json.loads(data)
        
        try:
            # 存入mongodb中
            sheet.insert(item)
            print(u"Processing: %(name)s" % item)
        except :
            print(u"Error procesing: %r" % item)
def save_to_mysql():
    ''' 把redis数据库中的数据存入mysql 

        需要在mysql中手动创建数据库zhilian: create database zhilian;
        切换到指定数据库：use zhilian;
        创建表jobs以及所有字段的列名和数据类型
    '''
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db = 'zhilian', port=3306, use_unicode=True)

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["getjob:items"])
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句  在此仅简单测试一下
            cur.execute("INSERT INTO jobs (company, size, type_name) VALUES ( %s, %s, %s)"%(item['company'], item['size'], item['type_name']))
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print("inserted %s" % item['company'])
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
if __name__ == '__main__':
    # 需要注意的是 从redis中取出数据存到别的数据库中，redis中将不再有这个数据
    save_to_mongodb()
    
    # save_to_mysql()
    
    