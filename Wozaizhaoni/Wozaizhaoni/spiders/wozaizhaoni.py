# -*- coding: utf-8 -*-
import scrapy
import re
import json
from Wozaizhaoni.items import WozaizhaoniItem
pat = re.compile('pics = (.*?);var pids')
pat_userid = re.compile('index/(\d+)')
pat_age = re.compile("(\d+)岁")
class WozaizhaoniSpider(scrapy.Spider):
    name = 'wozaizhaoni'
    # allowed_domains = ['baidu.co']
    nan_headers = {
        'Host': 'www.95195.com',
# Connection: keep-alive
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# Accept-Encoding: gzip, deflate
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'PHPSESSID=m6c4s2gnctr2lp1d0tvkg3o115; Hm_lvt_3dec807f9dffb87bec1f7e48c2037bf2=1534838857; cookie_cert_nologin=2; card_newsearch015=MXwwfDB8MHwwfDB8MHzlubTpvoTkuI3pmZB85a2m5Y6G5LiN6ZmQfOWcsOWMuuS4jemZkHznlLc%3D; ckstatus0=1; SERVERID=a4e890ea6a947865454b5a7267f22b1c|1534844869|1534838881; Hm_lpvt_3dec807f9dffb87bec1f7e48c2037bf2=1534844845',
        # 'Cookie': 'PHPSESSID=m6c4s2gnctr2lp1d0tvkg3o115; Hm_lvt_3dec807f9dffb87bec1f7e48c2037bf2=1534838857; cookie_cert_nologin=2; ckstatus0=1; card_newsearch015=MHwwfDB8MHwxMDB8MHwwfOW5tOm%2BhOS4jemZkHzlrabljobkuI3pmZB85Zyw5Yy65LiN6ZmQfOWlsw%3D%3D; SERVERID=a4e890ea6a947865454b5a7267f22b1c|1534846164|1534838881; Hm_lpvt_3dec807f9dffb87bec1f7e48c2037bf2=1534846140',

    }
    url1 = 'http://www.95195.com/index/default/0/1/{}.html'
    url2 = 'http://www.95195.com/index/default/0/2/{}.html'
    url3 = 'http://www.95195.com/index/default/0/6/{}.html'
    urls = []
    for i in range(1,268):
        urls.append(url1.format(i))
        urls.append(url2.format(i))
        urls.append(url3.format(i))
    start_urls = urls

    """ 
    267页
   
男
1  http://www.95195.com/index/default/0/1/10.html
2  http://www.95195.com/index/default/0/2/6.html
3  http://www.95195.com/index/default/0/6/6.html
Cookie: PHPSESSID=m6c4s2gnctr2lp1d0tvkg3o115; Hm_lvt_3dec807f9dffb87bec1f7e48c2037bf2=1534838857; cookie_cert_nologin=2; card_newsearch015=MXwwfDB8MHwwfDB8MHzlubTpvoTkuI3pmZB85a2m5Y6G5LiN6ZmQfOWcsOWMuuS4jemZkHznlLc%3D; ckstatus0=1; SERVERID=a4e890ea6a947865454b5a7267f22b1c|1534844869|1534838881; Hm_lpvt_3dec807f9dffb87bec1f7e48c2037bf2=1534844845
女
1  http://www.95195.com/index/default/0/1/10.html
2  http://www.95195.com/index/default/0/2/6.html
3  http://www.95195.com/index/default/0/6/6.html

Cookie: PHPSESSID=m6c4s2gnctr2lp1d0tvkg3o115; Hm_lvt_3dec807f9dffb87bec1f7e48c2037bf2=1534838857; cookie_cert_nologin=2; ckstatus0=1; card_newsearch015=MHwwfDB8MHwxMDB8MHwwfOW5tOm%2BhOS4jemZkHzlrabljobkuI3pmZB85Zyw5Yy65LiN6ZmQfOWlsw%3D%3D; SERVERID=a4e890ea6a947865454b5a7267f22b1c|1534846164|1534838881; Hm_lpvt_3dec807f9dffb87bec1f7e48c2037bf2=1534846140

    """

    def parse(self, response):
        user_urls = response.xpath("//div[@class='listbox']//div[@class='pubublock']/a/@href").extract()
        for each in user_urls:
            user_url = 'http://www.95195.com'+ each
            yield scrapy.Request(url=user_url,headers=self.nan_headers,callback=self.parse_item)
    def parse_item(self,response):
        print(response.url)
        
        item = WozaizhaoniItem()
        
        image_url=[]
        try:
            item['user_id'] = pat_userid.findall(response.url)[0]
            age_text = response.xpath("//span[@class='font14 colorh6']/text()").extract()[0]
            item['age'] = pat_age.findall(age_text)[0]
            m=pat.findall(response.text)[0]
            pics = json.loads(m)
            for imgurl in pics:
                img = imgurl[:-12]
                image_url.append(img)
            if image_url:
                item['image_url'] = image_url
                yield item
        except Exception as e:
            print(e)
        