import scrapy
from url.items import UrlItem
import logging


class UrlSpider(scrapy.Spider):
  name = 'url'
  allowed_domains = ['http://www.youboy.com/']
  start_urls = ['http://qiye.youboy.com/type/800_{}.html#page={}'
                .format(i,i) for i in range(1,6)]

  def parse(self, response):
    item = UrlItem()
    urls = response.xpath('//li[@class="dqscontit"]')
    self.logger.info('使用的ip是：%s' % response.request)
    for u in urls:
      url = u.xpath('a/@href').extract()
      item['url'] = url
      print (item)
      yield item