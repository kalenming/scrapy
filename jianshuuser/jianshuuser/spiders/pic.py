# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import requests
import os
import xlrd


class PicSpider(Spider):
    index = 1
    name = "pic"
    allowed_domains = ["jianshu.io"]
    name = xlrd.open_workbook('fan.xlsx')
    sheet = name.sheet_by_name('Sheet2')
    urls = sheet.col_values(0)
    start_urls = urls


    def parse(self, response):
        file = '/pic/%d.jpg' % self.index
        fileimage = open(file,'wb')
        fileimage.write(response.text)
        fileimage.close()