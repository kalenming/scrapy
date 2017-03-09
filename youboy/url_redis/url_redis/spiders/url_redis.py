# -*- coding: utf-8 -*-
from url_redis.items import UrlRedisItem

from scrapy.dupefilters import RFPDupeFilter
from scrapy.spiders import CrawlSpider,Rule

class UrlredisSpider(CrawlSpider):
  name = "url_redis"
  allow_domains = "http://www.youboy.com/"

  start_urls = ['http://qiye.youboy.com/type/800_1.html#page=1',
                'http://qiye.youboy.com/type/800_1.html#page=1']

  def parse(self,response):
    item = UrlRedisItem()
    urls = response.xpath('//li[@class="dqscontit"]')
    #self.logger.info('使用的ip是：%s' % response.request)
    for u in urls:
      url = u.xpath('a/@href').extract()
      item['url'] = url
      print (item)
      yield item
