#encoding=UTF-8
import scrapy
import random
import re
import math
from Mafengwo.MysqlPipelines.pipelines import NumberCheck
import json
from scrapy.http import Request
from scrapy import FormRequest
from scrapy import Spider
from bs4 import BeautifulSoup
from Mafengwo.items import MafengwoItem
from urllib.parse import urlencode
from scrapy.conf import settings
class MafengwoSpider(Spider):
    name = "MafengwoSpider"
    # base_url = "http://www.mafengwo.cn/yj/10926/1-0-1.html"
    #base_url = "http://www.mafengwo.cn/u/5350202/note.html"
    #base_url="http://www.mafengwo.cn/u/zhanghuanxiang/note.html"
    #base_url = "http://www.mafengwo.cn/i/9543261.html"
    #base_url = "http://www.mafengwo.cn/u/5251090/note.html"
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
    
    citys = [17315,10156,10434,10010,10445,11534,10439,10089,10030,14786,10513,10132,12522,10039,11246,10684,10207,10140,10128,11729,10802,10804,10435,10088,10198,10269,13063,10095,10027,10796,11755,10453,18065,10442,10814,10073,10381,11932,14753,14484,10085,10195,10799,10800,19603,10240,10783,10076,11340,11353,13061,10444,10284,10805,10256,11243,11270,10443,10547,11241,10057,10087,10267,10024,10792,10133,10521,10489,10440,10825,10045,10589,10244,11465,11754,10209,11499,10432,11386,10449,10094,10632,10774,10390,10414,10068,10427,10127,10301,10584,10728,10819,21434,15325,11065,16405,23039,12594,10044,10222,10765,11042,11041,10746,10768,10769,16283,11043,15297,15298,61629,59480,19816,10766,11047,15284,11045,14210,16980,11046,16209,10754,10460,13752,10760,28411,11049,11051,16102,16315,16105,16359,11055,11053,10406,15308,15305,16113,16112,16114,10737,29500,16115,16117,10753,11068,33109,17748,17751,11214,11215,47029,49450,49111,11059,11061,11062,63702,11275,16126,16127,16120,16122,18034,16123,16125,10926,10742,10579,10077,10927,19016,10929,10745,10925,10917,10916,10928,11703,11124,11125,14784,16162,11129,11132,10063,11083,11087,11084,16428,10573,11122,11109,11110,11112,11108,10102,11133,11135,11138,21366,11142,11171,63452,11155,14635,15338,13006,11081,10958,10755,11080,35987,11091,18705,11167,16095,11143,11228,16876,18041,10761,11141,22351,11095,16084,62910,62907,105930,11100,11101,16099,11106,16100,10177,10160,11684,11656,11005,10448,11160,11157,10214,26909,11853,10855,10856,10858,19036,17339,10857,10865,10885,15920,11044,10344,11367,11185,51454,48718,16708,16077,113734,16078,113733,11761,16827,10029,17439]
    # base_urls = []
    # for code in city:
    #     base_url = "http://www.mafengwo.cn/yj/%s"%code
    #     base_urls.append(base_url)
    oset = {'http://www.mafengwo.cn/yj/28411/1-0-173.html', 'http://www.mafengwo.cn/yj/10136/1-0-156.html', 'http://www.mafengwo.cn/yj/10284/1-0-22.html', 'http://www.mafengwo.cn/yj/10445/1-0-93.html', 'http://www.mafengwo.cn/yj/10061/1-0-173.html', 'http://www.mafengwo.cn/yj/10865/1-0-8.html', 'http://www.mafengwo.cn/yj/10068/1-0-71.html', 'http://www.mafengwo.cn/yj/10521/1-0-85.html', 'http://www.mafengwo.cn/yj/11228/1-0-26.html', 'http://www.mafengwo.cn/yj/16105/1-0-1.html', 'http://www.mafengwo.cn/yj/10728/1-0-23.html', 'http://www.mafengwo.cn/yj/10320/1-0-173.html', 'http://www.mafengwo.cn/yj/10855/1-0-112.html', 'http://www.mafengwo.cn/yj/10208/1-0-148.html', 'http://www.mafengwo.cn/yj/16102/1-0-199.html', 'http://www.mafengwo.cn/yj/10444/1-0-108.html', 'http://www.mafengwo.cn/yj/10136/1-0-31.html', 'http://www.mafengwo.cn/yj/11160/1-0-18.html', 'http://www.mafengwo.cn/yj/10011/1-0-162.html', 'http://www.mafengwo.cn/yj/10487/1-0-112.html', 'http://www.mafengwo.cn/yj/10796/1-0-90.html', 'http://www.mafengwo.cn/yj/12522/1-0-90.html', 'http://www.mafengwo.cn/yj/10177/1-0-10.html', 'http://www.mafengwo.cn/yj/10121/1-0-12.html', 'http://www.mafengwo.cn/yj/10244/1-0-75.html', 'http://www.mafengwo.cn/yj/10746/1-0-169.html', 'http://www.mafengwo.cn/yj/28411/1-0-84.html', 'http://www.mafengwo.cn/yj/10584/1-0-25.html', 'http://www.mafengwo.cn/yj/10121/1-0-134.html', 'http://www.mafengwo.cn/yj/10453/1-0-99.html', 'http://www.mafengwo.cn/yj/10156/1-0-100.html', 'http://www.mafengwo.cn/yj/10095/1-0-161.html', 'http://www.mafengwo.cn/yj/10076/1-0-38.html', 'http://www.mafengwo.cn/yj/10132/1-0-41.html', 'http://www.mafengwo.cn/yj/10865/1-0-12.html', 'http://www.mafengwo.cn/yj/10088/1-0-110.html', 'http://www.mafengwo.cn/yj/13061/1-0-61.html', 'http://www.mafengwo.cn/yj/11100/1-0-11.html', 'http://www.mafengwo.cn/yj/10916/1-0-6.html', 'http://www.mafengwo.cn/yj/10958/1-0-40.html', 'http://www.mafengwo.cn/yj/11122/1-0-49.html', 'http://www.mafengwo.cn/yj/10444/1-0-154.html', 'http://www.mafengwo.cn/yj/15950/1-0-4.html', 'http://www.mafengwo.cn/yj/11045/1-0-154.html', 'http://www.mafengwo.cn/yj/10085/1-0-60.html', 'http://www.mafengwo.cn/yj/10651/1-0-7.html', 'http://www.mafengwo.cn/yj/11386/1-0-6.html', 'http://www.mafengwo.cn/yj/10027/1-0-12.html', 'http://www.mafengwo.cn/yj/10796/1-0-78.html', 'http://www.mafengwo.cn/yj/10753/1-0-12.html', 'http://www.mafengwo.cn/yj/10133/1-0-34.html', 'http://www.mafengwo.cn/yj/10195/1-0-131.html', 'http://www.mafengwo.cn/yj/10198/1-0-172.html', 'http://www.mafengwo.cn/yj/10256/1-0-18.html', 'http://www.mafengwo.cn/yj/11047/1-0-125.html', 'http://www.mafengwo.cn/yj/10045/1-0-91.html', 'http://www.mafengwo.cn/yj/10222/1-0-194.html', 'http://www.mafengwo.cn/yj/21434/1-0-58.html', 'http://www.mafengwo.cn/yj/10513/1-0-16.html', 'http://www.mafengwo.cn/yj/10765/1-0-68.html', 'http://www.mafengwo.cn/yj/10796/1-0-140.html', 'http://www.mafengwo.cn/yj/10865/1-0-10.html', 'http://www.mafengwo.cn/yj/10244/1-0-63.html', 'http://www.mafengwo.cn/yj/10240/1-0-3.html', 'http://www.mafengwo.cn/yj/10076/1-0-2.html', 'http://www.mafengwo.cn/yj/11042/1-0-92.html', 'http://www.mafengwo.cn/yj/12522/1-0-34.html', 'http://www.mafengwo.cn/yj/10925/1-0-2.html', 'http://www.mafengwo.cn/yj/10198/1-0-13.html', 'http://www.mafengwo.cn/yj/10088/1-0-123.html', 'http://www.mafengwo.cn/yj/10432/1-0-81.html', 'http://www.mafengwo.cn/yj/28411/1-0-139.html', 'http://www.mafengwo.cn/yj/10010/1-0-142.html', 'http://www.mafengwo.cn/yj/10073/1-0-8.html', 'http://www.mafengwo.cn/yj/10521/1-0-72.html', 'http://www.mafengwo.cn/yj/10076/1-0-34.html', 'http://www.mafengwo.cn/yj/11243/1-0-133.html', 'http://www.mafengwo.cn/yj/10802/1-0-40.html', 'http://www.mafengwo.cn/yj/11171/1-0-5.html', 'http://www.mafengwo.cn/yj/10320/1-0-45.html', 'http://www.mafengwo.cn/yj/17315/1-0-6.html', 'http://www.mafengwo.cn/yj/10449/1-0-23.html', 'http://www.mafengwo.cn/yj/21434/1-0-35.html', 'http://www.mafengwo.cn/yj/10444/1-0-197.html', 'http://www.mafengwo.cn/yj/10573/1-0-158.html', 'http://www.mafengwo.cn/yj/10807/1-0-184.html', 'http://www.mafengwo.cn/yj/10929/1-0-24.html', 'http://www.mafengwo.cn/yj/10063/1-0-40.html', 'http://www.mafengwo.cn/yj/10435/1-0-46.html', 'http://www.mafengwo.cn/yj/10136/1-0-126.html', 'http://www.mafengwo.cn/yj/10195/1-0-18.html', 'http://www.mafengwo.cn/yj/15284/1-0-189.html', 'http://www.mafengwo.cn/yj/10094/1-0-10.html', 'http://www.mafengwo.cn/yj/10584/1-0-4.html', 'http://www.mafengwo.cn/yj/11042/1-0-129.html', 'http://www.mafengwo.cn/yj/10453/1-0-162.html', 'http://www.mafengwo.cn/yj/10800/1-0-45.html', 'http://www.mafengwo.cn/yj/10442/1-0-187.html', 'http://www.mafengwo.cn/yj/10284/1-0-76.html', 'http://www.mafengwo.cn/yj/10132/1-0-98.html', 'http://www.mafengwo.cn/yj/10039/1-0-60.html', 'http://www.mafengwo.cn/yj/16114/1-0-4.html', 'http://www.mafengwo.cn/yj/10065/1-0-55.html', 'http://www.mafengwo.cn/yj/10819/1-0-139.html', 'http://www.mafengwo.cn/yj/10482/1-0-55.html', 'http://www.mafengwo.cn/yj/10445/1-0-11.html', 'http://www.mafengwo.cn/yj/10448/1-0-9.html', 'http://www.mafengwo.cn/yj/11045/1-0-2.html', 'http://www.mafengwo.cn/yj/15284/1-0-144.html', 'http://www.mafengwo.cn/yj/16113/1-0-11.html', 'http://www.mafengwo.cn/yj/10453/1-0-55.html', 'http://www.mafengwo.cn/yj/10076/1-0-10.html', 'http://www.mafengwo.cn/yj/11046/1-0-48.html', 'http://www.mafengwo.cn/yj/11132/1-0-1.html', 'http://www.mafengwo.cn/yj/10198/1-0-174.html'}
    
    aset = set()
    for city in citys:
        for i in range(200): #根据目的地游记页面数量
            url = "http://www.mafengwo.cn/yj/%s/1-0-%s.html"%(city,i+1)
            aset.add(url)

    # remainPages=NumberCheck.find_remain_pages(alist) # 未抓取页数
    remain = aset-oset
    def start_requests(self):
        for url in self.remain:
            headers = {
                'User-Agent': random.choice(self.pc_agents)
            }
            yield Request(url, meta = {'page_url':url},headers=headers,callback=self.getAuthor,dont_filter=True)
            # dont_filter需要改一下

    def getAuthor(self, response): #抓用户
        print(response.url)
        soup = BeautifulSoup(response.text,'lxml')
        items = soup.find_all('span', attrs={'class': "author"})
        #print(items)
        #item = response.meta['item']
        #print(items)
        for each in items:
            pattern = re.compile('a href="(.*?)" rel',re.S)
            urls = re.findall(pattern, str(each))
            urls.pop()
            for url in urls:
                userId = url.split('.')[0].split('/')[-1]
                newUrl = "http://www.mafengwo.cn" + url.split('.')[0]+"/note.html"
                # print(newUrl)
                headers = {
                    'User-Agent': random.choice(self.pc_agents)
                }
                yield Request(newUrl,headers=headers, callback=self.getAuthorPage,meta={"userId":userId,'page_url': response.meta['page_url']})

    def getAuthorPage(self, response):#抓用户页面，游记
        soup = BeautifulSoup(response.text, 'lxml')
        articles = soup.find_all('div', attrs={'class': "note_info"})
        pattern = re.compile('<a href="(.*?)"', re.S)
        userId = response.meta['userId']
        for article in articles:
            articleUrl = re.findall(pattern, str(article))
            #print(articleUrl)
            articleUrl = articleUrl.pop()
            url = "http://www.mafengwo.cn" + articleUrl
            articleId = articleUrl.split('/')[-1].replace('.html', "")
            # print(url)
            # print(articleId)
            headers = {
                'User-Agent': random.choice(self.pc_agents)
            }
            yield Request(url,headers=headers, meta={"articleId" : articleId, "userId": userId,'page_url': response.meta['page_url']},callback=self.getImgs)
        items = soup.find_all('div', attrs={'class': "MAvaNums"})
        item = items.pop(0)
        # print(item)
        pattern = re.compile('<strong>(.*?)<.*?>游记', re.S)
        articleNum = re.findall(pattern, str(item))
        articleNum = articleNum.pop()
        totalPage = 0
        if int(articleNum) > 10:
            totalPage = int(articleNum) / 10
            totalPage = math.ceil(totalPage)
        else:
            totalPage = 1
        #print(articleNum)
        #print(totalPage)
        currentPage = soup.find_all('span', attrs={'class': "pg-current"})
        pattern = re.compile('>(.*?)<', re.S)
        currentNum = re.findall(pattern, str(currentPage))
        currentNum = currentNum.pop()
        #print("当前页数")
        #print(currentNum)
        if int(currentNum)!=int(totalPage):
            currentNum = str(int(currentNum)+1)
            #print(currentNum)
            #print("当前url")
            #print(response.url)
            userId = response.meta["userId"]
            # print(userId)
            headers = {
                'User-Agent': random.choice(self.pc_agents)
            }
            yield FormRequest(
                url = "http://www.mafengwo.cn/wo/ajax_post.php",
                formdata={"sAction": "getArticle",
                          "iPage": currentNum,
                          "iUid": userId },
                headers=headers,
                callback = self.getAuthorPageAfter,
                meta = {"currentPage": currentNum,
                        "totalPage": totalPage,
                        "userId" : userId,
                        'page_url': response.meta['page_url']}
            )
    def getAuthorPageAfter(self, response):#用户页面翻页
        #print(response.text)
        pattern = re.compile('u003ca href=\\\\"(.*?)\\\\"')
        items = re.findall(pattern, response.text)
        currentNum = response.meta["currentPage"]
        totalPage = response.meta["totalPage"]
        userId = response.meta["userId"]
        for item in items:
            url = item.replace("\\","")
            newUrl = "http://www.mafengwo.cn"+ url
            # print(newUrl)
            articleId = newUrl.split('/')[-1].replace('.html',"")
            # print(articleId)
            headers = {
                'User-Agent': random.choice(self.pc_agents)
            }
            yield Request(newUrl, headers=headers, meta={"articleId" : articleId, "userId": userId,'page_url': response.meta['page_url']}, callback=self.getImgs)
        if int(currentNum) != int(totalPage):
            currentNum = str(int(currentNum) + 1)
            headers = {
                'User-Agent': random.choice(self.pc_agents)
            }
            yield FormRequest(
                # response = response,
                url="http://www.mafengwo.cn/wo/ajax_post.php",
                formdata={"sAction": "getArticle",
                          "iPage": currentNum,
                          "iUid": userId},
                headers=headers,
                callback=self.getAuthorPageAfter,
                meta={"currentPage": currentNum,
                      "totalPage": totalPage,
                        "userId" : userId,
                      'page_url': response.meta['page_url']}
            )

    def getImgs(self, response):#从游记中获取img
        #print(response.text)
        # print(response.url)
        soup = BeautifulSoup(response.text,'html.parser')
        #print(soup.prettify())
        items = soup.find_all('p', attrs={'class': "_j_note_content _j_seqitem"})
        #print(response.meta["articleId"])
        #print(items)
        pattern = re.compile('data-seq="(.*?)">', re.S)
        data_seqs= re.findall(pattern, str(items))
        userId = response.meta['userId']
        # print(userId)
        # print(data_seqs)
        if data_seqs != []:
            data_seq = data_seqs.pop()
            # print(data_seq)
            articles = soup.find_all('a', attrs={'style': "display: block"})
            # print(articles)
            pattern = re.compile('<img.*?src="(.*?)\?image.*?" data', re.S)
            #item = response.meta['item']
            img = re.findall(pattern, str(articles))
            # print(img)
            #print(userId)
            articleId = response.meta['articleId']
            params = {
                'act': 'getNoteDetailContentChunk',
                'id': articleId,
                'seq': data_seq,
                'back': '0'
            }
            headers = {
                'User-Agent': random.choice(self.pc_agents)
            }
            url = "http://www.mafengwo.cn/note/ajax.php?" + urlencode(params)
            yield Request(url, headers=headers,meta={'articleId': articleId, 'userId': userId, 'img_urls':img,'page_url': response.meta['page_url']}, callback=self.getImgsAfter)


    def getImgsAfter(self, response):#游记翻页
        #print(response.text)
        item = json.loads(response.text)
        html = item['data']['html']
        has_more = item['data']['has_more']
        #print(type(has_more))
        img_urls = response.meta['img_urls']
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('img')
        pattern = re.compile('data-rt-src="(.*?)\?image.*?"')
        # print(soup.prettify())
        #item = response.meta['item']

        #print(item)
        userId = response.meta['userId']
        page_url = response.meta['page_url']
        imgs = re.findall(pattern, str(items))
        # print(imgs)
        img_urls = list(set(img_urls+imgs))

        if has_more:
            nextPage = soup.find_all('p', attrs={'class': "_j_note_content _j_seqitem"})
            pattern = re.compile('data-seq="(.*?)"', re.S)
            data_seqs = re.findall(pattern, str(nextPage))
            #print(data_seqs)
            data_seq = data_seqs.pop()
            #print(data_seq)
            articleId = response.meta['articleId']
            params = {
                'act': 'getNoteDetailContentChunk',
                'id': articleId,
                'seq': data_seq,
                'back': '0'
            }
            url = "http://www.mafengwo.cn/note/ajax.php?" + urlencode(params)
            headers = {
                'User-Agent': random.choice(self.pc_agents)
            }
            yield Request(url, headers=headers,meta={'articleId': articleId,'userId': userId,'img_urls':img_urls,'page_url': response.meta['page_url']},
                          callback=self.getImgsAfter)
        else:
            item = MafengwoItem()
            articleId = response.meta['articleId']
            # print(img_urls)
            # print("userId: %s"%userId)
            item['image_urls'] = img_urls
            item['userID'] = userId
            item['articleID'] = articleId
            # item['page_urls'] = page_url
            # print("Num of images: %s"%len(img_urls))
            # print("article ID: %s"%articleId)

            if item['image_urls']:
                yield item

