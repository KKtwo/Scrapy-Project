# -*- coding: utf-8 -*-

# Scrapy settings for Wozaizhaoni project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Wozaizhaoni'

SPIDER_MODULES = ['Wozaizhaoni.spiders']
NEWSPIDER_MODULE = 'Wozaizhaoni.spiders'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 暂停功能
SCHEDULER_PERSIST = True
# 调度队列 :请求的优先级
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
DOWNLOAD_DELAY = 0.2
CONCURRENT_REQUESTS = 40
# DOWNLOADS_TIMEOUT = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 50
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Wozaizhaoni (+http://www.yourdomain.com)'
COOKIES_ENABLED = False
IMAGES_STORE = "G:/wozaizhaoni"
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'Host': 'www.95195.com',
# Connection: keep-alive
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# Accept-Encoding: gzip, deflate
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 男
    # 'Cookie': 'PHPSESSID=m6c4s2gnctr2lp1d0tvkg3o115; Hm_lvt_3dec807f9dffb87bec1f7e48c2037bf2=1534838857; cookie_cert_nologin=2; card_newsearch015=MXwwfDB8MHwwfDB8MHzlubTpvoTkuI3pmZB85a2m5Y6G5LiN6ZmQfOWcsOWMuuS4jemZkHznlLc%3D; ckstatus0=1; SERVERID=a4e890ea6a947865454b5a7267f22b1c|1534844869|1534838881; Hm_lpvt_3dec807f9dffb87bec1f7e48c2037bf2=1534844845',
    # 女
    # 'Cookie': 'PHPSESSID=m6c4s2gnctr2lp1d0tvkg3o115; Hm_lvt_3dec807f9dffb87bec1f7e48c2037bf2=1534838857; cookie_cert_nologin=2; ckstatus0=1; card_newsearch015=MHwwfDB8MHwxMDB8MHwwfOW5tOm%2BhOS4jemZkHzlrabljobkuI3pmZB85Zyw5Yy65LiN6ZmQfOWlsw%3D%3D; SERVERID=a4e890ea6a947865454b5a7267f22b1c|1534846164|1534838881; Hm_lpvt_3dec807f9dffb87bec1f7e48c2037bf2=1534846140'

}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Wozaizhaoni.middlewares.WozaizhaoniSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Wozaizhaoni.middlewares.WozaizhaoniDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Wozaizhaoni.pipelines.WozaizhaoniPipeline': 300,
#}
DOWNLOADER_MIDDLEWARES = {

    'Wozaizhaoni.middlewares.ABProxyMiddleware':300
}

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
ITEM_PIPELINES = {
    'Wozaizhaoni.pipelines.WozaizhaoniPipeline': 400,
    'scrapy_redis.pipelines.RedisPipeline': 300,
}
LOG_LEVEL= 'DEBUG'

LOG_FILE ='log_8_22_nv.log'
# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
