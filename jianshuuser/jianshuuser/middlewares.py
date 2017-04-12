import random
import base64
import os

def proxy_ip():
    proxys = list()
    with open(r'ip\host.txt','r') as f:
        lines = f.readlines()
    for l in lines:
        line = l.strip('\r\n')
        dict = {'ip_port':line,'user_pass':''}
        proxys.append(dict)
    return proxys

class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        print ("**************************" + random.choice(self.agents))
        request.headers.setdefault('User-Agent', random.choice(self.agents))

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        PROXIES = proxy_ip()
        proxy = random.choice(PROXIES)
        print ("**************ProxyMiddleware no pass************" + proxy['ip_port'])
        request.meta['proxy'] = "http://%s" % proxy['ip_port']