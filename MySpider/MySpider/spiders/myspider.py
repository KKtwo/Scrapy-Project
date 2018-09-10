# -*- coding: utf-8 -*-
import scrapy
import json
import re
import requests
from scrapy.spiders import Spider
from MySpider.items import MyspiderItem


class MySpider(Spider):
    name = 'myspider'
    # allowed_domains = [
    #     'jp.match.com',
    #     'securepictures.match.com',
    # ]

    # }
    # 待爬
    # page = 1
    # gender = 2
    # seekingGender = 1
    # code_list = [52,17,25,2,48,9,15,41,11,36,4,20,30,46,16,7,50,27,10,39,1,24,37,23,14,29,51,45,38,32,12,49,43,18,5,21,8,35,28,22,31,26,19,33]
    
    # code = 24

    # code = 13
    # name  shortName page
    countryCodes = [1,2,3,4,5,6,7,9,10,11,8,12,13,14,15,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,35,300,36,38,37,301,39,40,41,42,44,43,45,46,47,48,49,50,51,52,54,58,59,60,63,61,62,64,65,67,68,69,70,71,74,75,76,78,79,81,82,84,85,86,87,88,90,91,92,93,94,95,96,98,99,100,101,102,302,104,106,109,108,110,111,112,113,115,116,304,117,119,120,121,305,123,126,127,128,129,130,131,132,134,135,308,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,173,174,175,177,178,179,180,181,182,183,184,306,185,186,187,191,192,193,194,195,188,197,198,199,307,200,201,202,203,205,206,209,207,208,210,77,309,211,212,213,214,215,216,217,218,219,220,221,222,223,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240]
    search_url = "http://cn.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A{}%2C%22seekingGender%22%3A{}%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22postalCode%22%3A%22%22%2C%22state%22%3A%7B%22countryCode%22%3A{}%2C%22code%22%3A{}%2C%22name%22%3A%22Shanghai%22%2C%22shortName%22%3A%22%22%7D%2C%22country%22%3A%7B%22code%22%3A{}%2C%22name%22%3A%22China%22%2C%22shortName%22%3A%22CHN%22%7D%2C%22distance%22%3A5000%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22cities%22%3A%5B%7B%22countryCode%22%3A{}%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%7D%5D%2C%22locationFullName%22%3A%22N%2FA%2C%20N%2FA%22%2C%22page%22%3A1%7D;logImpressions=true?locale=en-US&returnMeta=true"
    # .format(gender,seekingGender,countryCode,code,countryCode,countryCode,page)
    
    sheaders = {
        'Host': 'cn.match.com',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'ADRUM': 'isAjax:true',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
        # 'Accept': '*/*',
        'Referer': 'http://cn.match.com/search',
        'Accept-Language': 'zh-CN,zh;q=0.9',

    }
    allheaders = {
        'Host': 'cn.match.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'ADRUM': 'isAjax:true',
        'X-Requested-By': 'legacy',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
        'Referer': 'http://cn.match.com/dnws/accountsettings/accountindex.aspx',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '_ga=GA1.2.1005446955.1533704451; __gads=ID=a012f4591fca78ea:T=1533704471:S=ALNI_MamZE82eDbFgEg1zaYPOb64XaZU9Q; IsRegistered=true; IsRegisteredDomain=true; dUserType=2; dCUserType=registered; __ssid=66f217ae-0b57-478f-9fc7-047b293491e3; cto_lwid=3013aeba-87f4-4715-a714-b7574615dacb; MAT=dHQsmTgeiAGVsKxFNS0xPGCXlMOjN0HLSiVHrI8Mj-01; _gid=GA1.2.220349676.1534212128; MatchSession=UMID=98298e0c-14a7-4061-b93a-6e271b9216bd&CDTF=8/14/2018; UserType=2; machineid=da97e80e-ddaa-4938-8094-b9cf10821ce3; CUserType=registered; __utmz=191932533.1534317178.9.6.utmcsr=wiki.hobot.cc|utmccn=(referral)|utmcmd=referral|utmcct=/pages/viewpage.action; searchparams=%7B%22gender%22%3A1%2C%22seekingGender%22%3A2%2C%22minAge%22%3A25%2C%22maxAge%22%3A35%2C%22postalCode%22%3A%2290210%22%2C%22distance%22%3A50%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22certifiedOnly%22%3Afalse%2C%22availableForChat%22%3Afalse%7D; ISHC=cn.match.com; OLN=OLNVAL=0; MatchSearch2=K03=25&K04=35&K11=0&K12=&K14=1034474&K15=-1&K16=43&K01=2&K02=1&K08=&K17=1; dMatchSearch2=K11=0&K12=&K14=1034474&K15=-1&K16=43&K17=1&K03=25&K04=35&K08=&K01=2&K02=1; rm=true; Mat_mkt=ct=1&fvs=8/14/2018&lvs=8/16/2018&prf=2&pic=1&mgen=1&gsk=2&ag=1&agsk=1; Handle=dHQsmTgeiAGVsKxFNS0xPEePzY4tMaoK0; Password=C-UdQnv54sLTbwcotj_CEQ2; Match=CCount=13&CDate=8/16/2018&uid=JsKogzS5F_PSGHuGx_815Q2; dMatch=CCount=13&CDate=8/16/2018; authtoken=rMvGFAD3hrabQxa%2BlT3JawqNIwyXOQmmu6WcAnQYmKBTnazh3FV%2Be%2BRmTHKmP8p%2FwfEfODd742elzCao0pwnskaln0tfxHJiFPGcokS2lJngZYroSilCTapmHNaKUnSq%2CMatchFD51DE89D449%2C12%2C49; uid=JsKogzS5F_PSGHuGx_815Q2; session=j%3A%7B%22sid%22%3A%2268ac5ea9-5edc-4bdc-b157-76efab44f121%22%2C%22theme%22%3A%22207%22%2C%22token%22%3A%22rMvGFAD3hrabQxa%2BlT3JawqNIwyXOQmmu6WcAnQYmKBTnazh3FV%2Be%2BRmTHKmP8p%2FwfEfODd742elzCao0pwnskaln0tfxHJiFPGcokS2lJngZYroSilCTapmHNaKUnSq%2CMatchFD51DE89D449%2C12%2C49%22%7D; _gat=1; OX_sd=1; SECU=TID=527905&ESID=00000000-0000-0000-0000-000000000000&THEME=0; R-Transfer=rUri=WsSBPK5yhh10OfdUAJ5v2A2&rTkn=rMvGFAD3hrabQxa%2BlT3JawqNIwyXOQmmu6WcAnQYmKBTnazh3FV%2Be%2BRmTHKmP8p%2FwfEfODd742elzCao0pwnskaln0tfxHJiFPGcokS2lJngZYroSilCTapmHNaKUnSq%2CMatchFD51DE89D449%2C12%2C49; __utma=191932533.1005446955.1533704451.1534414590.1534471889.14; __utmc=191932533; __utmt=1; __utmb=191932533.1.10.1534471889',
        
    }
    # start_urls = urls
    page_pat=re.compile(r'page%22%3A(\d+)')
    gender_sub=re.compile(r'gender%22%3A\d+')
    seekingGender_sub=re.compile(r'seekingGender%22%3A\d+')
    pat= re.compile(r'page=(\d+)')
    def start_requests(self):

        with open('D:\code\MySpider\start_url.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                url = line.strip()
                yield scrapy.Request(url=url,headers=self.sheaders,dont_filter=True,callback=self.parse)

    def parse(self, response):
        # print(response.url)
        page = int(self.page_pat.findall(response.url)[0])
        
        # 获取json数据
        body = json.loads(response.body.decode('utf-8'))
        # 提取
        items = body['data']['items']
        print('page = %s'%page,'items%s'%len(items))
        # 遍历  每个item都是一个字典
        for each in items:
            item = MyspiderItem()
            item['user_id'] = each['userId']
            # print(item['user_id'])
            item['age'] = each['age']
            user_url = "https://jp.match.com/profile/%s?page=%s&searchType=oneWaySearch&sortBy=1" % (each['userId'],page)
            # print('user_url--',user_url)
            # 发送每个请求，获取详细信息,并把item传递过去
            yield scrapy.Request(url=user_url,meta={'item': item},callback=self.parse_item)
            # print('end')
        # 发送每个页面请求
        if items:
            page += 1
            url = self.page_pat.sub("page%22%3A{}".format(page),response.url)
            yield scrapy.Request(url=url, callback=self.parse)

    # 处理每个页面的数据
    def parse_item(self, response):
        print(response.url)
        # 首先获取到item
        item = response.meta['item']
        pattern = re.compile(
            r'"photosByProfileId"\S+profileSimilaritiesByProfileId"')
        m = pattern.search(response.body.decode('utf-8'))
        # 构造json字符串
        json_str = '{' + m.group().split(
            ',"profileSimilaritiesByProfileId"')[0] + '}'
        image_json = json.loads(json_str)
        image_items = image_json['photosByProfileId'][item['user_id']]['items']
        image_urls = []
        for image in image_items:
            image_url = "https://securepictures.match.com/photos/600/700/{}.jpeg?lang=ja-JP".format(
                image)
            image_urls.append(image_url)
            
        item['image_url'] = image_urls
        yield item
