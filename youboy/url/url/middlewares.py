import base64
import random
import logging


class ProxyMiddleware(object):

  def process_request(self, request, spider):
    proxys = [
      '106.46.136.76:808',
      '106.46.136.199:808',
      '106.46.136.193:808',
      '106.46.136.152:808',
      '106.46.136.58:808',
      '106.46.136.29:808',
      '119.5.1.12:808',
      '123.157.146.116:8123',
      '106.46.136.4:808',
      '106.46.136.89:808',
      '124.88.67.63:80',
      '124.42.7.103:80',
      '106.46.136.246:808',
      '101.81.120.58:8118',
      '124.88.67.21:843',
      '124.88.67.14:80',
      '101.200.43.84:8118',
      '223.155.124.93:80',
      '121.204.165.176:8118',
      '119.254.84.90:80',
      '106.46.136.141:808',
      '119.5.0.124:808'
    ]
    proxy_address = random.choice(proxys)
    self.logger.info('访问ip：%s' % proxy_address)
    request.meta['proxy'] = proxy_address


  def process_exception(self, request, exception, spider):
    proxy = request.meta['proxy']
    self.logger.info('Removing failed proxy <%s>, %d proxies left' % (
      proxy, len(self.proxies)))
    try:
      del self.proxies
    except ValueError:
      pass
