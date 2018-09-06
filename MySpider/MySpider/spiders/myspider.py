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
    # headers = {
    #     'Host': 'jp.match.com',
    #     'Connection': 'keep-alive',
    #     'X-Requested-With': 'XMLHttpRequest',
    #     'ADRUM': 'isAjax:true',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
    #     'Accept': '*/*',
    #     'Referer': 'https://jp.match.com/search?lid=2&st=Q',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Cookie': 'MatchSession=UMID=4e746fa4-77dd-4ec2-b701-d67cb8690f2a&CDTF=8/1/2018; cto_lwid=e65bdacd-cfb0-4a24-b5a2-a071abf5eb1c; machineid=c290f795-a351-4e5a-8447-2105aaaea335; OLN=OLNVAL=0; ISHC=jp.match.com; MAT=dHQsmTgeiAGVsKxFNS0xPGCXlMOjN0HLSiVHrI8Mj-01; Handle=dHQsmTgeiAGVsKxFNS0xPEePzY4tMaoK0; IsRegistered=true; IsRegisteredLoginCounter=0; CUserType=registered; dCUserType=registered; _ga=GA1.2.1255920880.1533106440; _gid=GA1.2.2130663105.1533192414; __utmz=191932533.1533194785.3.3.utmcsr=wiki.hobot.cc|utmccn=(referral)|utmcmd=referral|utmcct=/pages/viewpage.action; __ssid=9a6284fc-64b4-4daa-a719-9dbacb41d54f; rm=true; Handle=dHQsmTgeiAGVsKxFNS0xPEePzY4tMaoK0; IsRegistered=true; IsRegisteredDomain=true; UserType=2; dUserType=2; Password=C-UdQnv54sLTbwcotj_CEQ2; MatchSearch2=K01=2&K02=1&K03=18&K04=36&K11=0&K12=&K14=1750372&K15=13&K16=109&K17=1; dMatchSearch2=K01=2&K02=1&K08=&K11=0&K12=&K15=13&K16=109&K17=1&K21=0&K22=0&K03=18&K04=36&K14=1750372; Mat_mkt=ct=1&fvs=8/1/2018&lvs=8/3/2018&prf=2&pic=&mgen=2&gsk=1&ag=1&agsk=1; __utma=191932533.1255920880.1533106440.1533197389.1533273149.5; Match=CCount=6&CDate=8/3/2018&uid=JhEAYdHnZcxw8rAOM_cHtw2; dMatch=CCount=6&CDate=8/3/2018; SECU=TID=527568&ESID=47b0c9dc-62af-47ff-a7e5-3029fe03389d&THEME=210; __utmc=191932533; uid=JhEAYdHnZcxw8rAOM_cHtw2; searchparams=%7B%22gender%22%3A2%2C%22seekingGender%22%3A1%2C%22minAge%22%3A18%2C%22maxAge%22%3A30%2C%22postalCode%22%3A%22%22%2C%22state%22%3A%7B%22countryCode%22%3A109%2C%22hasCities%22%3Atrue%2C%22code%22%3A13%2C%22name%22%3A%22%E5%8C%97%E6%B5%B7%E9%81%93%22%2C%22shortName%22%3A%22%E5%8C%97%E6%B5%B7%E9%81%93%22%7D%2C%22country%22%3A%7B%22hasStates%22%3Atrue%2C%22hasCities%22%3Atrue%2C%22code%22%3A109%2C%22name%22%3A%22%E6%97%A5%E6%9C%AC%22%2C%22shortName%22%3A%22%E6%97%A5%E6%9C%AC%22%7D%2C%22distance%22%3A5000%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22locationFullName%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%2C%20%E5%8C%97%E6%B5%B7%E9%81%93%2C%20%E6%97%A5%E6%9C%AC%22%2C%22cities%22%3A%5B%7B%22countryCode%22%3A109%2C%22stateCode%22%3A13%2C%22latitude%22%3A43.823782%2C%22longitude%22%3A144.107042%2C%22code%22%3A1750372%2C%22name%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%22%2C%22shortName%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%22%7D%5D%7D; OX_plg=pm; __gads=ID=16667090e1d29c0b:T=1533273485:S=ALNI_MbQYiXh98O4nfBt-OzAvUd5LvZ2LQ; ADRUM=s=1533273971814&r=https%3A%2F%2Fjp.match.com%2Fsearch%3F192645693; __utmb=191932533.4.10.1533273149; authtoken=W4Q9W4NvK9udoh%2Fc6iV%2BxXhe8YaytMVdbki2dNjpANNuYBiKQq4FXkSk54ZuJDqEzgHthuQtAnl6AzH8AbvnnzAIrCyYF2n%2BYVggKurTjavXZIzfglFq9v4%2B%2FONTESNf%2CMatchFD51DE89D449%2C12%2C49; session=j%3A%7B%22sid%22%3A%2247b0c9dc-62af-47ff-a7e5-3029fe03389d%22%2C%22theme%22%3A%22210%22%2C%22token%22%3A%22W4Q9W4NvK9udoh%2Fc6iV%2BxXhe8YaytMVdbki2dNjpANNuYBiKQq4FXkSk54ZuJDqEzgHthuQtAnl6AzH8AbvnnzAIrCyYF2n%2BYVggKurTjavXZIzfglFq9v4%2B%2FONTESNf%2CMatchFD51DE89D449%2C12%2C49%22%2C%22rUri%22%3A%22http%3A%2F%2Fjp.match.com%22%7D; searchimpressions=%7B%22s%22%3A14%2C%22p%22%3A%5B3%5D%7D',
    
    # }
    # 待爬
    # page = 1
    # gender = 2
    # seekingGender = 1
    # code_list = [52,17,25,2,48,9,15,41,11,36,4,20,30,46,16,7,50,27,10,39,1,24,37,23,14,29,51,45,38,32,12,49,43,18,5,21,8,35,28,22,31,26,19,33]
    
    # code = 24

    # code = 13
    # name  shortName page
    # url = 'https://jp.match.com/api/discover-one-way;criteria={"sortBy":1,"gender":%s,"seekingGender":%s,"minAge":18,"maxAge":120,"state":{"countryCode":109,"code":%s,"name":"北海道,"shortName":"北海道"},"country":{"code":109,"name":"日本","shortName":"日本"},"isOnlineNow":false,"withPhotos":true,"availableForChat":false,"locationFullName":"網走郡美幌町, 北海道, 日本","cities":[{"countryCode":109,"code":"","name":"","shortName":""}],"refined":{"Keyword":""},"distance":5000,"postalCode":"","page":%s};logImpressions=true?locale=ja-JP&returnMeta=true'%(gender,seekingGender,code,page)
    # url = "https://jp.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A{}%2C%22seekingGender%22%3A{}%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22state%22%3A%7B%22countryCode%22%3A109%2C%22code%22%3A{}%2C%22name%22%3A%22%E5%A4%A7%E9%98%AA%E5%BA%9C%22%2C%22shortName%22%3A%22%E5%A4%A7%E9%98%AA%E5%BA%9C%22%7D%2C%22country%22%3A%7B%22code%22%3A109%2C%22name%22%3A%22%E6%97%A5%E6%9C%AC%22%2C%22shortName%22%3A%22%E6%97%A5%E6%9C%AC%22%7D%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22locationFullName%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%2C%20%E5%8C%97%E6%B5%B7%E9%81%93%2C%20%E6%97%A5%E6%9C%AC%22%2C%22cities%22%3A%5B%7B%22countryCode%22%3A109%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%2C%22shortName%22%3A%22%22%7D%5D%2C%22refined%22%3A%7B%22Keyword%22%3A%22%22%7D%2C%22distance%22%3A5000%2C%22postalCode%22%3A%22%22%2C%22page%22%3A{}%7D;logImpressions=true?locale=ja-JP&returnMeta=true".format(gender,seekingGender,code,page)
    # url = "https://jp.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A{}%2C%22seekingGender%22%3A{}%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22state%22%3A%7B%22countryCode%22%3A109%2C%22code%22%3A{}%2C%22name%22%3A%22%E5%A4%A7%E9%98%AA%E5%BA%9C%22%2C%22shortName%22%3A%22%E5%A4%A7%E9%98%AA%E5%BA%9C%22%7D%2C%22country%22%3A%7B%22code%22%3A109%2C%22name%22%3A%22%E6%97%A5%E6%9C%AC%22%2C%22shortName%22%3A%22%E6%97%A5%E6%9C%AC%22%7D%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22locationFullName%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%2C%20%E5%8C%97%E6%B5%B7%E9%81%93%2C%20%E6%97%A5%E6%9C%AC%22%2C%22cities%22%3A%5B%7B%22countryCode%22%3A109%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%2C%22shortName%22%3A%22%22%7D%5D%2C%22refined%22%3A%7B%22Keyword%22%3A%22%22%7D%2C%22distance%22%3A5000%2C%22postalCode%22%3A%22%22%2C%22page%22%3A{}%7D;logImpressions=true?locale=ja-JP&returnMeta=true".format(gender,seekingGender,code,page)
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
        # all_url = 'http://cn.match.com/MainService//GetAllCountries'
        # response_all = requests.get(url=all_url,headers=self.allheaders)
        # all_country = json.loads(response_all.text)
        # for country in all_country:
        #     if country['HasStates']:
        #         curl = 'http://cn.match.com/MainService//GetStatesByCountryCode?countryCode='+str(country['Code'])
        #     else:
        #         curl = 'http://cn.match.com/MainService//GetCitiesByCountryCode?countryCode='+str(country['Code'])
        with open('D:\code\MySpider\start_url.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                url = line.strip()
                yield scrapy.Request(url=url,headers=self.sheaders,dont_filter=True,callback=self.parse)
    # def get_city(self,response):
    #     print(response.url,response.status)
    #     countryCode=response.meta['countryCode']
    #     citys = json.loads(response.body.decode('utf-8'))
    #     try:
    #         for city in citys:
    #             code = city['Code']
    #             for gender in range(1,3):
    #                 for seekingGender in range(1,3):
    #                     yield scrapy.Request(url=self.search_url.format(gender,seekingGender,countryCode,code,countryCode,countryCode),headers=self.sheaders,callback=self.parse)
    #     except:
    #         print('获取城市Code出错！---')
    #         print(citys)
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
