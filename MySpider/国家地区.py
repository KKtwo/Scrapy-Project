import requests
import json
import random
# import scrapy
# response_all = scrapy.Request(url=all_url,headers=sheaders)
# scrapy.Request不直接返回response
# countryCodes = [1,2,3,4,5,6,7,9,10,11,8,12,13,14,15,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,35,300,36,38,37,301,39,40,41,42,44,43,45,46,47,48,49,50,51,52,54,58,59,60,63,61,62,64,65,67,68,69,70,71,74,75,76,78,79,81,82,84,85,86,87,88,90,91,92,93,94,95,96,98,99,100,101,102,302,104,106,109,108,110,111,112,113,115,116,304,117,119,120,121,305,123,126,127,128,129,130,131,132,134,135,308,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,173,174,175,177,178,179,180,181,182,183,184,306,185,186,187,191,192,193,194,195,188,197,198,199,307,200,201,202,203,205,206,209,207,208,210,77,309,211,212,213,214,215,216,217,218,219,220,221,222,223,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240]
# gender = 1 # 女
# seekingGender = 2 # 男
# countryCode = 1
# code = 1
# page = 1

# curl = 'http://cn.match.com/MainService//GetCitiesByCountryCode?countryCode=240'
# 获取每个城市代码
# [{"Name":"Anhui","Code":1,"Abbreviation":null,"HasCities":true},{"Name":"Fujian","Code":2,"Abbreviation":null,"HasCities":true},{"Name":"Gansu","Code":3,"Abbreviation":null,"HasCities":true},{"Name":"Guangdong","Code":4,"Abbreviation":null,"HasCities":true},{"Name":"Guangxi","Code":5,"Abbreviation":null,"HasCities":true},{"Name":"Guizhou","Code":6,"Abbreviation":null,"HasCities":true},{"Name":"Hebei","Code":7,"Abbreviation":null,"HasCities":true},{"Name":"Heilongjiang","Code":8,"Abbreviation":null,"HasCities":true},{"Name":"Henan","Code":9,"Abbreviation":null,"HasCities":true},{"Name":"Hubei","Code":10,"Abbreviation":null,"HasCities":true},{"Name":"Hunan","Code":11,"Abbreviation":null,"HasCities":true},{"Name":"Jiangsu","Code":12,"Abbreviation":null,"HasCities":true},{"Name":"Jiangxi","Code":13,"Abbreviation":null,"HasCities":true},{"Name":"Jilin","Code":14,"Abbreviation":null,"HasCities":true},{"Name":"Liaoning","Code":15,"Abbreviation":null,"HasCities":true},{"Name":"Nei Mongol","Code":16,"Abbreviation":null,"HasCities":true},{"Name":"Ningxia","Code":17,"Abbreviation":null,"HasCities":true},{"Name":"Quinghai","Code":18,"Abbreviation":null,"HasCities":true},{"Name":"Shaanxi","Code":19,"Abbreviation":null,"HasCities":true},{"Name":"Shandong","Code":20,"Abbreviation":null,"HasCities":true},{"Name":"Shanxi","Code":21,"Abbreviation":null,"HasCities":true},{"Name":"Sichuan","Code":22,"Abbreviation":null,"HasCities":true},{"Name":"Xinjiang Uygur","Code":23,"Abbreviation":null,"HasCities":true},{"Name":"Xizang","Code":24,"Abbreviation":null,"HasCities":true},{"Name":"Yunnan","Code":25,"Abbreviation":null,"HasCities":true},{"Name":"Zhejiang","Code":26,"Abbreviation":null,"HasCities":true},{"Name":"Beijing","Code":27,"Abbreviation":null,"HasCities":true},{"Name":"Chongqing","Code":28,"Abbreviation":null,"HasCities":false},{"Name":"Taiwan","Code":29,"Abbreviation":null,"HasCities":true},{"Name":"Shanghai","Code":30,"Abbreviation":null,"HasCities":true},{"Name":"Tianjin","Code":31,"Abbreviation":null,"HasCities":true},{"Name":"Hainan","Code":32,"Abbreviation":null,"HasCities":false},{"Name":"Hong-Kong","Code":33,"Abbreviation":null,"HasCities":true},{"Name":"Macau","Code":34,"Abbreviation":null,"HasCities":true}]
# search_url = "https://jp.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A{}%2C%22seekingGender%22%3A{}%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22state%22%3A%7B%22countryCode%22%3A109%2C%22code%22%3A{}%2C%22name%22%3A%22%E5%A4%A7%E9%98%AA%E5%BA%9C%22%2C%22shortName%22%3A%22%E5%A4%A7%E9%98%AA%E5%BA%9C%22%7D%2C%22country%22%3A%7B%22code%22%3A109%2C%22name%22%3A%22%E6%97%A5%E6%9C%AC%22%2C%22shortName%22%3A%22%E6%97%A5%E6%9C%AC%22%7D%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22locationFullName%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%2C%20%E5%8C%97%E6%B5%B7%E9%81%93%2C%20%E6%97%A5%E6%9C%AC%22%2C%22cities%22%3A%5B%7B%22countryCode%22%3A109%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%2C%22shortName%22%3A%22%22%7D%5D%2C%22refined%22%3A%7B%22Keyword%22%3A%22%22%7D%2C%22distance%22%3A5000%2C%22postalCode%22%3A%22%22%2C%22page%22%3A{}%7D;logImpressions=true?locale=ja-JP&returnMeta=true".format(gender,seekingGender,code,page)
# search_url = "http://cn.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A{}%2C%22seekingGender%22%3A{}%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22postalCode%22%3A%22%22%2C%22state%22%3A%7B%22countryCode%22%3A{}%2C%22code%22%3A{}%2C%22name%22%3A%22Shanghai%22%2C%22shortName%22%3A%22%22%7D%2C%22country%22%3A%7B%22code%22%3A{}%2C%22name%22%3A%22China%22%2C%22shortName%22%3A%22CHN%22%7D%2C%22distance%22%3A5000%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22cities%22%3A%5B%7B%22countryCode%22%3A{}%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%7D%5D%2C%22locationFullName%22%3A%22N%2FA%2C%20N%2FA%22%2C%22page%22%3A{}%7D;logImpressions=true?locale=en-US&returnMeta=true".format(gender,seekingGender,countryCode,code,countryCode,countryCode,page)
# s_url = "http://cn.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A2%2C%22seekingGender%22%3A1%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22postalCode%22%3A%22%22%2C%22state%22%3A%7B%22countryCode%22%3A43%2C%22code%22%3A30%2C%22name%22%3A%22Shanghai%22%2C%22shortName%22%3A%22%22%7D%2C%22country%22%3A%7B%22code%22%3A43%2C%22name%22%3A%22China%22%2C%22shortName%22%3A%22CHN%22%7D%2C%22distance%22%3A5000%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22cities%22%3A%5B%7B%22countryCode%22%3A43%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%7D%5D%2C%22locationFullName%22%3A%22N%2FA%2C%20N%2FA%22%2C%22page%22%3A1%7D;logImpressions=true?locale=en-US&returnMeta=true"

chrome_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'ADRUM': 'isAjax:true',
    'Cookie': '_ga=GA1.2.1005446955.1533704451; __gads=ID=a012f4591fca78ea:T=1533704471:S=ALNI_MamZE82eDbFgEg1zaYPOb64XaZU9Q; IsRegistered=true; IsRegisteredDomain=true; dUserType=2; dCUserType=registered; __ssid=66f217ae-0b57-478f-9fc7-047b293491e3; cto_lwid=3013aeba-87f4-4715-a714-b7574615dacb; MAT=dHQsmTgeiAGVsKxFNS0xPGCXlMOjN0HLSiVHrI8Mj-01; _gid=GA1.2.220349676.1534212128; MatchSession=UMID=98298e0c-14a7-4061-b93a-6e271b9216bd&CDTF=8/14/2018; UserType=2; machineid=da97e80e-ddaa-4938-8094-b9cf10821ce3; CUserType=registered; __utmz=191932533.1534317178.9.6.utmcsr=wiki.hobot.cc|utmccn=(referral)|utmcmd=referral|utmcct=/pages/viewpage.action; searchparams=%7B%22gender%22%3A1%2C%22seekingGender%22%3A2%2C%22minAge%22%3A25%2C%22maxAge%22%3A35%2C%22postalCode%22%3A%2290210%22%2C%22distance%22%3A50%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22certifiedOnly%22%3Afalse%2C%22availableForChat%22%3Afalse%7D; ISHC=cn.match.com; OLN=OLNVAL=0; MatchSearch2=K03=25&K04=35&K11=0&K12=&K14=1034474&K15=-1&K16=43&K01=2&K02=1&K08=&K17=1; dMatchSearch2=K11=0&K12=&K14=1034474&K15=-1&K16=43&K17=1&K03=25&K04=35&K08=&K01=2&K02=1; rm=true; Mat_mkt=ct=1&fvs=8/14/2018&lvs=8/16/2018&prf=2&pic=1&mgen=1&gsk=2&ag=1&agsk=1; Handle=dHQsmTgeiAGVsKxFNS0xPEePzY4tMaoK0; Password=C-UdQnv54sLTbwcotj_CEQ2; Match=CCount=13&CDate=8/16/2018&uid=JsKogzS5F_PSGHuGx_815Q2; dMatch=CCount=13&CDate=8/16/2018; authtoken=rMvGFAD3hrabQxa%2BlT3JawqNIwyXOQmmu6WcAnQYmKBTnazh3FV%2Be%2BRmTHKmP8p%2FwfEfODd742elzCao0pwnskaln0tfxHJiFPGcokS2lJngZYroSilCTapmHNaKUnSq%2CMatchFD51DE89D449%2C12%2C49; uid=JsKogzS5F_PSGHuGx_815Q2; session=j%3A%7B%22sid%22%3A%2268ac5ea9-5edc-4bdc-b157-76efab44f121%22%2C%22theme%22%3A%22207%22%2C%22token%22%3A%22rMvGFAD3hrabQxa%2BlT3JawqNIwyXOQmmu6WcAnQYmKBTnazh3FV%2Be%2BRmTHKmP8p%2FwfEfODd742elzCao0pwnskaln0tfxHJiFPGcokS2lJngZYroSilCTapmHNaKUnSq%2CMatchFD51DE89D449%2C12%2C49%22%7D; _gat=1; OX_sd=1; SECU=TID=527905&ESID=00000000-0000-0000-0000-000000000000&THEME=0; R-Transfer=rUri=WsSBPK5yhh10OfdUAJ5v2A2&rTkn=rMvGFAD3hrabQxa%2BlT3JawqNIwyXOQmmu6WcAnQYmKBTnazh3FV%2Be%2BRmTHKmP8p%2FwfEfODd742elzCao0pwnskaln0tfxHJiFPGcokS2lJngZYroSilCTapmHNaKUnSq%2CMatchFD51DE89D449%2C12%2C49; __utma=191932533.1005446955.1533704451.1534414590.1534471889.14; __utmc=191932533; __utmt=1; __utmb=191932533.1.10.1534471889',

    'Host': 'cn.match.com',
    'Referer': 'http://cn.match.com/accountsettings/accountindex.aspx?lid=3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
    'X-Requested-By': 'legacy',
    'X-Requested-With': 'XMLHttpRequest',
}
# curl = 'http://cn.match.com/MainService//GetCitiesByCountryCode?countryCode='+str(countryCode)
proxies = []
PROXY_MSG1 = {''}
PROXY_MSG2 = {''}
PROXY_MSG3 = {''}
proxies.append(PROXY_MSG1)
proxies.append(PROXY_MSG2)
proxies.append(PROXY_MSG3)
search_url = "http://cn.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A{}%2C%22seekingGender%22%3A{}%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22postalCode%22%3A%22%22%2C%22state%22%3A%7B%22countryCode%22%3A{}%2C%22code%22%3A{}%2C%22name%22%3A%22Shanghai%22%2C%22shortName%22%3A%22%22%7D%2C%22country%22%3A%7B%22code%22%3A{}%2C%22name%22%3A%22China%22%2C%22shortName%22%3A%22CHN%22%7D%2C%22distance%22%3A5000%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22cities%22%3A%5B%7B%22countryCode%22%3A{}%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%7D%5D%2C%22locationFullName%22%3A%22N%2FA%2C%20N%2FA%22%2C%22page%22%3A1%7D;logImpressions=true?locale=en-US&returnMeta=true"

start_url = []
error_url = []
def get_city(url,countryCode):
    response = requests.get(url=url,headers=chrome_headers,proxies=random.choice(proxies))
    print(response.url,response.status_code)
    # countryCode=response.meta['countryCode']
    try:
        citys = json.loads(response.text)
        for city in citys:
            code = city['Code']
            for gender in range(1,3):
                for seekingGender in range(1,3):
                    url=search_url.format(gender,seekingGender,countryCode,code,countryCode,countryCode)
                    start_url.append(url+'\n')
    except Exception as e:
        print('获取城市Code出错！---')
        print(e)
        error_url.append(response.url)
def get_country():

    all_url = 'http://cn.match.com/MainService//GetAllCountries'
    response_all = requests.get(url=all_url)
    all_country = json.loads(response_all.text)
    # print(all_country)
    for country in all_country:
        if country['HasStates']:
            curl = 'http://cn.match.com/MainService//GetStatesByCountryCode?countryCode='+str(country['Code'])
        else:
            curl = 'http://cn.match.com/MainService//GetCitiesByCountryCode?countryCode='+str(country['Code'])
        get_city(curl,country['Code'])

get_country()
# 用writelines可以把列表里的字符串取出来写入，加入\n换行
with open('start_url.txt','w',encoding='utf-8') as f:
    f.writelines(start_url)

# # print(country['HasStates'])
# # curl='http://cn.match.com/MainService//GetCitiesByCountryCode?countryCode=139'
# curl = 'http://cn.match.com/MainService//GetStatesByCountryCode?countryCode=1'
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
url = 'http://cn.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A1%2C%22seekingGender%22%3A2%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22postalCode%22%3A%22%22%2C%22state%22%3A%7B%22countryCode%22%3A33%2C%22code%22%3A1207168%2C%22name%22%3A%22Shanghai%22%2C%22shortName%22%3A%22%22%7D%2C%22country%22%3A%7B%22code%22%3A33%2C%22name%22%3A%22China%22%2C%22shortName%22%3A%22CHN%22%7D%2C%22distance%22%3A5000%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22cities%22%3A%5B%7B%22countryCode%22%3A33%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%7D%5D%2C%22locationFullName%22%3A%22N%2FA%2C%20N%2FA%22%2C%22page%22%3A1%7D;logImpressions=true?locale=en-US&returnMeta=true'
url = 'http://cn.match.com/api/discover-one-way;criteria=%7B%22sortBy%22%3A1%2C%22gender%22%3A1%2C%22seekingGender%22%3A2%2C%22minAge%22%3A18%2C%22maxAge%22%3A120%2C%22postalCode%22%3A%22%22%2C%22state%22%3A%7B%22countryCode%22%3A5%2C%22code%22%3A1454612%2C%22name%22%3A%22Shanghai%22%2C%22shortName%22%3A%22%22%7D%2C%22country%22%3A%7B%22code%22%3A5%2C%22name%22%3A%22China%22%2C%22shortName%22%3A%22CHN%22%7D%2C%22distance%22%3A5000%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22cities%22%3A%5B%7B%22countryCode%22%3A5%2C%22code%22%3A%22%22%2C%22name%22%3A%22%22%7D%5D%2C%22locationFullName%22%3A%22N%2FA%2C%20N%2FA%22%2C%22page%22%3A2%7D;logImpressions=true?locale=en-US&returnMeta=true'

response = requests.get(url=url,headers=sheaders,proxies = random.choice(proxies))

print(response.url,response.status_code)
# response = requests.get(url=curl,headers=sheaders)
# data = json.loads(response.text)
# print(data)
print(response.text)