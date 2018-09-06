# -*- coding: utf-8 -*-

# Scrapy settings for MySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MySpider'

SPIDER_MODULES = ['MySpider.spiders']
NEWSPIDER_MODULE = 'MySpider.spiders'

# 使用scrapy-redis的去重模块
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 暂停功能
SCHEDULER_PERSIST = True
# 调度队列 :请求的优先级
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 先进先出
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈 后进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MySpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 0.2
CONCURRENT_REQUESTS = 40
# DOWNLOADS_TIMEOUT = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 50
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'Host': 'jp.match.com',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'ADRUM': 'isAjax:true',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://jp.match.com/search?lid=2&st=Q',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'MatchSession=UMID=4e746fa4-77dd-4ec2-b701-d67cb8690f2a&CDTF=8/1/2018; cto_lwid=e65bdacd-cfb0-4a24-b5a2-a071abf5eb1c; machineid=c290f795-a351-4e5a-8447-2105aaaea335; OLN=OLNVAL=0; ISHC=jp.match.com; MAT=dHQsmTgeiAGVsKxFNS0xPGCXlMOjN0HLSiVHrI8Mj-01; Handle=dHQsmTgeiAGVsKxFNS0xPEePzY4tMaoK0; IsRegistered=true; IsRegisteredLoginCounter=0; CUserType=registered; dCUserType=registered; _ga=GA1.2.1255920880.1533106440; _gid=GA1.2.2130663105.1533192414; __utmz=191932533.1533194785.3.3.utmcsr=wiki.hobot.cc|utmccn=(referral)|utmcmd=referral|utmcct=/pages/viewpage.action; __ssid=9a6284fc-64b4-4daa-a719-9dbacb41d54f; rm=true; Handle=dHQsmTgeiAGVsKxFNS0xPEePzY4tMaoK0; IsRegistered=true; IsRegisteredDomain=true; UserType=2; dUserType=2; Password=C-UdQnv54sLTbwcotj_CEQ2; MatchSearch2=K01=2&K02=1&K03=18&K04=36&K11=0&K12=&K14=1750372&K15=13&K16=109&K17=1; dMatchSearch2=K01=2&K02=1&K08=&K11=0&K12=&K15=13&K16=109&K17=1&K21=0&K22=0&K03=18&K04=36&K14=1750372; Mat_mkt=ct=1&fvs=8/1/2018&lvs=8/3/2018&prf=2&pic=&mgen=2&gsk=1&ag=1&agsk=1; __utma=191932533.1255920880.1533106440.1533197389.1533273149.5; Match=CCount=6&CDate=8/3/2018&uid=JhEAYdHnZcxw8rAOM_cHtw2; dMatch=CCount=6&CDate=8/3/2018; SECU=TID=527568&ESID=47b0c9dc-62af-47ff-a7e5-3029fe03389d&THEME=210; __utmc=191932533; uid=JhEAYdHnZcxw8rAOM_cHtw2; searchparams=%7B%22gender%22%3A2%2C%22seekingGender%22%3A2%2C%22minAge%22%3A18%2C%22maxAge%22%3A30%2C%22postalCode%22%3A%22%22%2C%22state%22%3A%7B%22countryCode%22%3A109%2C%22hasCities%22%3Atrue%2C%22code%22%3A13%2C%22name%22%3A%22%E5%8C%97%E6%B5%B7%E9%81%93%22%2C%22shortName%22%3A%22%E5%8C%97%E6%B5%B7%E9%81%93%22%7D%2C%22country%22%3A%7B%22hasStates%22%3Atrue%2C%22hasCities%22%3Atrue%2C%22code%22%3A109%2C%22name%22%3A%22%E6%97%A5%E6%9C%AC%22%2C%22shortName%22%3A%22%E6%97%A5%E6%9C%AC%22%7D%2C%22distance%22%3A5000%2C%22isOnlineNow%22%3Afalse%2C%22withPhotos%22%3Atrue%2C%22availableForChat%22%3Afalse%2C%22locationFullName%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%2C%20%E5%8C%97%E6%B5%B7%E9%81%93%2C%20%E6%97%A5%E6%9C%AC%22%2C%22cities%22%3A%5B%7B%22countryCode%22%3A109%2C%22stateCode%22%3A13%2C%22latitude%22%3A43.823782%2C%22longitude%22%3A144.107042%2C%22code%22%3A1750372%2C%22name%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%22%2C%22shortName%22%3A%22%E7%B6%B2%E8%B5%B0%E9%83%A1%E7%BE%8E%E5%B9%8C%E7%94%BA%22%7D%5D%7D; OX_plg=pm; __gads=ID=16667090e1d29c0b:T=1533273485:S=ALNI_MbQYiXh98O4nfBt-OzAvUd5LvZ2LQ; ADRUM=s=1533273971814&r=https%3A%2F%2Fjp.match.com%2Fsearch%3F192645693; __utmb=191932533.4.10.1533273149; authtoken=W4Q9W4NvK9udoh%2Fc6iV%2BxXhe8YaytMVdbki2dNjpANNuYBiKQq4FXkSk54ZuJDqEzgHthuQtAnl6AzH8AbvnnzAIrCyYF2n%2BYVggKurTjavXZIzfglFq9v4%2B%2FONTESNf%2CMatchFD51DE89D449%2C12%2C49; session=j%3A%7B%22sid%22%3A%2247b0c9dc-62af-47ff-a7e5-3029fe03389d%22%2C%22theme%22%3A%22210%22%2C%22token%22%3A%22W4Q9W4NvK9udoh%2Fc6iV%2BxXhe8YaytMVdbki2dNjpANNuYBiKQq4FXkSk54ZuJDqEzgHthuQtAnl6AzH8AbvnnzAIrCyYF2n%2BYVggKurTjavXZIzfglFq9v4%2B%2FONTESNf%2CMatchFD51DE89D449%2C12%2C49%22%2C%22rUri%22%3A%22http%3A%2F%2Fjp.match.com%22%7D; searchimpressions=%7B%22s%22%3A14%2C%22p%22%3A%5B3%5D%7D',
    
}
IMAGES_STORE = "F:\match\Images"
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'MySpider.middlewares.MyspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#   'MySpider.middlewares.ABProxyMiddleware': 300,
# #     随机代理ip
# #   'MySpider.middlewares.RandomProxy':300,
# }
# DOWNLOADER_MIDDLEWARES = {
#   'NanSpider.middlewares.NanspiderDownloaderMiddleware': 543,
#     随机代理ip
#   'NanSpider.middlewares.RandomProxy':300,
    # 'MySpider.middlewares.ABProxyMiddleware':300
# }
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'MySpider.pipelines.MyspiderPipeline': 400,
    'scrapy_redis.pipelines.RedisPipeline': 300,
}
LOG_LEVEL= 'DEBUG'

LOG_FILE ='log_8_17.txt'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
