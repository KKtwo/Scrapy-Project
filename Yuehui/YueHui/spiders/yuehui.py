# -*- coding: utf-8 -*-
import scrapy
import json
import re
from YueHui.items import YuehuiItem
pat= re.compile(r'page=(\d+)')
img_pat=re.compile('<img id="vuser-asthumblist.*?src="(http.*?\d)"', re.S)
class YuehuiSpider(scrapy.Spider):
    name = 'yuehui'
    # allowed_domains = ['yuehui.163.com','yuehui1.nos.netease.com']
    # 循环page
    json_url = 'http://yuehui.163.com/searchusersrcm.do?ajax=1&ageBegin=18&ageEnd=89&aim=-1&marriage=-1&mode=1&order=11&province={}&city=0&district=-1&sex={}&userTag=0&vippage=-1&searchType=0&page=1&pagesize=75'
    # 从json获取用户id，拼接user_url
    # user_url = 'http://yuehui.163.com/viewuser.do?id=617576502'
    # 从用户页面获取//li/a/img
    # img_url = 'http://yuehui1.nos.netease.com/6/2/65/b42c2dc2379323ae4aeec46cbb837713/617576502/1526287232209'
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     'Cookie': '__f_=1533118505490; _ntes_nnid=c194d790973ab6a9a2a468d4a5f93ddf,1533118507484; _ntes_nuid=c194d790973ab6a9a2a468d4a5f93ddf; NTES_PASSPORT=IJugYLCNLro0QgyO4TCRxh4ZMBl.B4J39x8IsAA1tdLME_XDPEyXqNWqQduVEZLjtt5p3Qv7k2r0XjwtUzFlgsUTRG7qwHewhJZHWl.V5bN_Cjl3QqETaMYQf4ORFt_iZUjwPkQlAfiF5i_YjNGucBziJ1kIZt7lv.UkEGBDW5U2D; P_INFO=yi93952858584@163.com|1533710220|1|mail163|00&99|null&null&null#bej&null#10#0#0|&0||yi93952858584@163.com; nts_mail_user=yi93952858584@163.com:-1:1; mail_psc_fingerprint=3464f28fbde65d5ca8cfcaa139bb7e2e; usertrack=CrH7dVtqj6JRmEM8AwYMAg==; __utma=187553192.1996937057.1533721998.1533721998.1533721998.1; __utmz=187553192.1533721998.1.1.utmcsr=open.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __oc_uuid=e061e260-9af0-11e8-b2ba-f5a2ed85f65d; NTES_CMT_USER_INFO=260706340%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0fyx0A%7C%7Cfalse%7CeWk5Mzk1Mjg1ODU4NEAxNjMuY29t; idate_province=1; idate_city=0; search_photos_700072114=sex%3D0%26province%3D0%26city%3D0%26ageBegin%3D18%26ageEnd%3D23%26order%3D14; NTES_SESS=aW5QeW6mMX9aRLLdNUFXiM8xxBeTXZam0S3jMzLA49md3X6Zb3l6uEFuKt8N3QqLslwyAIbL5q1gg0dwIizJuSxkTi7D2jkWb9NogksL9T42VbIFUVPf.jeDtWFlkg6ZEa1Z6UOzb6O.Zs.yx_UJIAQA5QC60td2FzuygchQ2vdqF2sOHM7hrQ78g; S_INFO=1534298068|1|0&0##|yi93952858584; ANTICSRF=834248c577305df0611ca03388eb92e0; idateuid=700072114; idate_emsex=0; JSESSIONID=9A0C8ECDAFE3182132DA93F533DEC195; sid=7000721143YZg5z4PZoLqQ1ACECRW0CQMwJtArooHG4bXtA78qdGAtn3IhTvbSc6pOdhybJuA; cm_newmsg=user%3Dyi93952858584%40163.com%26new%3D18%26total%3D20',
    #     'Host': 'yuehui.163.com',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
    # }
    def start_requests(self):
        for sex in range(2):
            for province in range(34):
                url = self.json_url.format(province,sex)
                yield scrapy.Request(url,callback=self.parse)
    def parse(self, response):
        print(response.url,response.status)
        data=json.loads(response.body.decode('utf-8'))[0]
        # total = data['total']
        item_list = data['list']
        img_count=0
        for person in item_list:
            item = YuehuiItem()
            item['user_id'] = person['id']
            item['age'] = person['age']
            albumCount = person['albumCount']
            img_count = albumCount
            if albumCount>0:
                user_url = 'http://yuehui.163.com/viewuser.do?id=%s' %item['user_id']
                yield scrapy.Request(url=user_url,meta={'item':item},callback=self.parse_item)
        if img_count>0:
            page = int(pat.findall(response.url)[0])
            page+=1
            url = pat.sub("page=%s"%page,response.url)
            yield scrapy.Request(url,callback=self.parse)
    def parse_item(self,response):
        item = response.meta['item']
        # image_url = response.xpath("//li/a/img/@src").extract()
        image_url = img_pat.findall(response.body.decode('utf-8'))
        item['image_url'] = image_url
        if image_url:
            yield item
