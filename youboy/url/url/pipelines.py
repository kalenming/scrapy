# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy.exceptions import DropItem

class UrlPipeline(object):

    def __init__(self):
        self.ids_seen = set() #注意到set型数据的应用

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("url item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
