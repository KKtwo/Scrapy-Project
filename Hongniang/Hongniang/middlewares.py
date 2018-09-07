import base64
import random
""" 阿布云ip代理配置，包括账号密码 """
proxyServer = "http://http-dyn.abuyun.com:9020"

# for Python3
proxyAuths=[]



class ABProxyMiddleware(object):
    """ 阿布云ip代理配置 """
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = random.choice(proxyAuths)