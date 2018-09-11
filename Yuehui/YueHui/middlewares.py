import base64
import random
""" 阿布云ip代理配置，包括账号密码 """
proxyServer = "http://http-dyn.abuyun.com:9020"
proxyUser1 = "*****"
proxyPass1 = "*****"
proxyUser2 = "*****"
proxyPass2 = "*****"
proxyUser3 = "*****"
proxyPass3 = "*****"

# for Python3
proxyAuths=[]
proxyAuth1 = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser1 + ":" + proxyPass1), "ascii")).decode("utf8")
proxyAuth2 = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser2 + ":" + proxyPass2), "ascii")).decode("utf8")
proxyAuth3 = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser3 + ":" + proxyPass3), "ascii")).decode("utf8")
proxyAuths.append(proxyAuth1)
proxyAuths.append(proxyAuth2)
proxyAuths.append(proxyAuth3)


class ABProxyMiddleware(object):
    """ 阿布云ip代理配置 """
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = random.choice(proxyAuths)