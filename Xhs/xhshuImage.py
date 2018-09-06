# -*- coding:utf-8 -*-
import os
import requests
import json
import os
import re
import sys
import time
# import downloader
# import downloader as aiodownloader
from lxml import etree
# from downloader import launch_download
# from user_agent import pc_agents, mobile_agents
import random
from multiprocessing import Pool
from lxml.html import etree
import threadpool
from multiprocessing import Process,Pool
# import aiohttp #表示http请求是异步方式去请求的
import asyncio #当异步请求返回时,通知异步操作完成
import pymongo
from pymongo.errors import DuplicateKeyError
mongo = pymongo.MongoClient('127.0.0.1', 27017)
# from utils import save2mongo


pc_agents=[
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

session = requests.Session()

# //*[@class="by"]/cite/a/@href
# https://www.xiaohongshu.com/web_api/sns/v2/homefeed/notes?page_size=20&oid=recommend&page=2

PROXY_MSG = {'https':'https://HJ771V93F64YB5BD:93E7E414C82BEFB9@http-dyn.abuyun.com:9020', 'http':'http://HJ771V93F64YB5BD:93E7E414C82BEFB9@http-dyn.abuyun.com:9020'}

# 获取每个栏目的所有帖子
def get_columns_content(column_id):
    session.headers.update({
        'authority': 'www.xiaohongshu.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://www.xiaohongshu.com/explore?tab=%s'%column_id,
        'user-agent':random.choice(mobile_agents)
    })
    general_url = 'https://www.xiaohongshu.com/web_api/sns/v2/homefeed/notes?page_size=20&oid={}&page={}'

    page = 1
    while True:
        true_url = general_url.format(column_id, page)
        result = session.get(true_url).json()
        data = result['data']
        if len(data) < 1:
            break
        for item in data:
            uid = item['user']['id']
            print(uid)
            save2mongo(dbname='xhs', proj_name='xhs_user', imgs_urls=None, dirname=uid, parent_name=column_id)
        # for item in data:
        #     print("uid", item['user']['id'])
        #     get_user_all_items(item['user']['id'])
        #     time.sleep(0.6)
        page += 1
        time.sleep(random.choice([5, 6, 8, 9, 7]))

# 获取用户的所有帖子
def get_user_all_items(uid):
    time.sleep(1.2)
    session.headers.update({
        'Accept': 'application/json, text/plain, */*',
        'Host': 'www.xiaohongshu.com',
        'Referer': 'https://www.xiaohongshu.com/user/profile/%s' % uid,
        'User-Agent': random.choice(mobile_agents)
    })
    # https://www.xiaohongshu.com/web_api/sns/v1/user/52d8c541b4c4d60e6c867480/note?page=2
    general_user_url = 'https://www.xiaohongshu.com/web_api/sns/v1/user/{}/note?page={}'
    page = 1
    while True:
        user_next_page_url = general_user_url.format(uid, page)
        try:
            result = session.get(user_next_page_url).json()
        except json.decoder.JSONDecodeError:
            page += 1
            continue
        data = result['data']
        if len(data) < 1:
            break
        for item in data:
            print("item_id", item['id'])
            # parse_item_content(uid, item['id'])
            save2mongo(dbname='xhs', proj_name='xhs_all_item', imgs_urls=None, dirname=item['id'], parent_name=uid)
        time.sleep(random.choice([5, 5.5, 6.7, 5.8, 5.5]))
        page += 1
# {'_id': '5b5fd662910cf605182ab2a5', 'imgs_urls': None, 'proj_name': 'xhs_all_item', 'parent_name': '5aa6a105e8ac2b76aadfd4d5'}
# {'_id': '5b5ef6b6910cf605112af29a', 'imgs_urls': None, 'proj_name': 'xhs_all_item', 'parent_name': '5aa6a105e8ac2b76aadfd4d5'}
# {'_id': '5b5ed03a910cf6051a2b1355', 'imgs_urls': None, 'proj_name': 'xhs_all_item', 'parent_name': '5aa6a105e8ac2b76aadfd4d5'}
# {'_id': '5b5dd7f307ef1c7b55b7b190', 'imgs_urls': None, 'proj_name': 'xhs_all_item', 'parent_name': '5aa6a105e8ac2b76aadfd4d5'}
# 获取每个帖子的图像或视频
def parse_item_content(param):
    # params = param.split('_')
    uid, item_id = tiezi['parent_name'], tiezi['_id']
    # time.sleep(random.choice([5, 6, 6.5, 5.6, 6.7]))
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Host': 'www.xiaohongshu.com',
        'Referer': 'https://www.xiaohongshu.com/discovery/item/%s' % uid,
        'User-Agent': random.choice(pc_agents)
    }
    item_url = 'https://www.xiaohongshu.com/discovery/item/%s' % item_id

    
    # response = requests.get(item_url, headers=headers,proxies=PROXY_MSG)
    # print(response.status_code)
    # print(response.text)
    # selector = etree.HTML(response.text)
    # video = selector.xpath('//video/@src')
    # print('video:', video)
    # if len(video) > 0:
    #     save2mongo(dbname='xhs', proj_name='xhs_item_video', imgs_urls=video, dirname=item_id, parent_name=str(uid))
    #     print(video)

    # save2mongo(dbname='xhs', proj_name='xhs_items_except', imgs_urls=None, dirname=item_id, parent_name=str(uid))


        # url = 'https:'+video[0]
        # session.headers.update({
        #     'Referer': 'https://www.xiaohongshu.com/discovery/item/%s'%item_id,
        #     'User-Agent':random.choice(pc_agents)
        # })
        # response = session.get(url)
        # print(response.status_code)

        # save_dir = os.path.join('/Users/hangcong.li/Downloads/wangxin/xhs', uid)
        # if not os.path.exists(save_dir):
        #     os.makedirs(save_dir)
        # f = open(os.path.join(save_dir, '%s.mp4'%item_id), 'wb')
        # f.write(response.content)
        # f.close()
        # return
    # time.sleep(0.8)
    img_url = 'https://www.xiaohongshu.com/web_api/sns/v1/note/{}/image_stickers'
    img_link = img_url.format(item_id)
    try:
        result = requests.get(img_link, headers=headers, proxies=PROXY_MSG).json()
        print(result)
    except Exception:
        # result = requests.get(img_link, headers=headers, proxies=PROXY_MSG).json()
        # save2mongo(dbname='xhs', proj_name='xhs_items_except', imgs_urls=None, dirname=item_id, parent_name=str(uid))
        return
    data = result['data']
    genaral_img = 'http://ci.xiaohongshu.com/{}'
    true_imgs = []
    for item in data:
        fileid = item['fileid']
        print('uid', uid, 'fileid', fileid)
        true_img = genaral_img.format(fileid)
        true_imgs.append(true_img)
    # if len(true_imgs) > 1:
    #     ok = save2mongo(dbname='xhs', proj_name='xhs_items', imgs_urls=true_imgs, dirname=item_id, parent_name=str(uid))
    #     if ok:
    #         print(true_imgs)
    # else:
    #     save2mongo(dbname='xhs', proj_name='xhs_items_error', imgs_urls=None, dirname=item_id, parent_name=str(uid))
    # # time.sleep(0.6)



def launch_download(proj_name, imgs_urls, dirname, output_path):
    output_path = 'F:\\xhs\\Images'
    urls = {
        dirname: {}
    }
    for index, img in enumerate(imgs_urls):
        urls[dirname][img] = str(index)

    aiodownloader.launch_downloader(
        project_name=proj_name,
        urls=urls,
        output_path=output_path)


if __name__ == '__main__':
    # with open('xhs_images','r') as f:
    #     s=f.readline()
    #     print(s)

    # url = 'https://www.xiaohongshu.com/web_api/sns/v2/homefeed/notes?page_size=20&oid=recommend&page=3'85
    # all_urls = [url % index for index in range(1, 56)]
    # requests = threadpool.makeRequests(get_user_urls, all_urls)
    # [pool.putRequest(req) for req in requests]
    # pool.wait()
    # get_user_urls('https://www.xiaohongshu.com/web_api/sns/v2/homefeed/notes?page_size=20&oid=recommend&page=1')
    # get_video()
    # kword = ['food','recommend', 'fasion', 'cosmetics', 'sport', 'travel', 'home', 'babycare', 'mens_fasion', 'media']
    # for key in kword[8:]:
    #     get_columns_content(key)
    #     time.sleep(1.2)
    # limit_num = 3500
    # skip_num = 13500 #10000
    # data = mongo.xhs.xhs_user.find().limit(limit_num).skip(skip_num)#5180  7000
    # count = 0
    # for item in list(data):#203
    #     # print(count, limit_num)
    #     print(item['_id'])
    #     # get_user_all_items(item['_id'])
    #     count+=1
    #     time.sleep(0.8)

    # data = mongo.xhs.xhs_all_item.find()
    # with open('/Users/hangcong.li/Downloads/wangxin/xhs/xhs_all_item.txt', 'a') as f:
    #     for item in list(data):
    #         line = '%s\n' % (item)
    #         f.write(line)
    # count = 0
    # for item in list(data)[::-1]:#203
    #     print(count)
    #     print(item['_id'])
    #     parse_item_content('%s_%s' % (item['parent_name'], item['_id']))
    #     count+=1
    count_lines = 0
    with open("F:\\MySpider\\NanSpider\\xhs_all_items.txt",'r') as f:
            while True:
                line_str=f.readline()
                if line_str:
                    print(line_str)
                    count_lines+=1
                    line = line_str.strip('\n').replace("'",'"').replace("None",'""')
                    tiezi=json.loads(line)
                    parse_item_content(tiezi)
    # items = list(data)
    # p = Pool(4)           #开辟进程池
    # all_params = ['%s_%s' % (item['parent_name'], item['_id']) for item in items]
    # for param in all_params:
    #     p.apply_async(parse_item_content,args=(param,))#每个进程都调用run_proc函数，
                                                        #args表示给该函数传递的参数。

    # print 'Waiting for all subprocesses done ...'
    # p.close() #关闭进程池
    # p.join()  #等待开辟的所有进程执行完后，主进程才继续往下执行

    # pool = threadpool.ThreadPool(4)
    # data = mongo.xhs.xhs_all_item.find().limit(510).skip(3390)
    # items = list(data)
    # all_params = ['%s_%s' % (item['parent_name'], item['_id']) for item in items]
    #
    # # all_urls = [url % index for index in range(1, 56)]
    # reqs = threadpool.makeRequests(parse_item_content, all_params)
    # [pool.putRequest(req) for req in reqs]
    # pool.wait()
        # time.sleep(0.4)
