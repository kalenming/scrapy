# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class UrlRedisPipeline(object):
    def process_item(self, item, spider):
        return item

#
# from datetime import datetime
#
# class UrlRedisPipeline(object):
#     def process_item(self, item, spider):
#         item["crawled"] = datetime.utcnow()
#         item["spider"] = spider.name
#         return item