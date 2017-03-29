# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from jianshuuser.items import JianshuuserItem
from bs4 import BeautifulSoup


class JianshuSpider(Spider):
    name = "jianshu"
    allowed_domains = ["www.jianshu.com"]
    start_urls = [
        'http://www.jianshu.com/users/5SqsuF/followers?page={}' .format(i) for i in range(1,10878)
    ]

    # def start_requests(self):
    #     url = 'http://www.jianshu.com/users/5SqsuF/followers'
    #     yield Request(url,callback=self.parse)
    def parse(self, response):
        item = JianshuuserItem()
        soup = BeautifulSoup(response.text,'lxml')
        people = soup.select('li')
        print (people)
        for p in people:
            item['imgurl'] = p.select('.avatar > img')[0].get('src')
            item['name'] = p.select('.name')[0].text
            item['userurl'] = p.select('.name')[0].get('href')
            item['following'] = p.select('div > div')[0].select('span')[0].text
            item['followed'] = p.select('div > div')[0].select('span')[1].text
            item['articles'] = p.select('div > div')[0].select('span')[2].text
            item['essays'] = p.select('div > div')[0].select('span')[3].text
            item['details'] = p.select('div > div')[1].text
            yield item
