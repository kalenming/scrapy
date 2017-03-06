# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy.exceptions import DropItem

class UrlPipeline(object):

    def __init__(self):
        self.url = set() #注意到set型数据的应用

    def process_item(self, item, spider):
        if item['url'] in self.url:
            raise DropItem("url item found: %s" % item)
        else:
            self.url.add(item['url'])
            return item
