# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:17:19 2017

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import xlrd
import random


#获取代理ip
def proxies():
    os.chdir(r'C:\Users\Administrator\Desktop\scrapy\proxy')
    fp = open('host.txt','r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        ip =p.strip('\n').split('\t')
        proxy = 'http://' +  ip[0] + ':' + ip[1]
        proxies = {'proxy':proxy}
        proxys.append(proxies)
    return proxys

#从爬取到的文件中读取企业url
def read_url():
    os.chdir(r'C:\Users\Administrator\Desktop\scrapy\scrapy\youboy')
    workbook = xlrd.open_workbook('1.xls')
    sheet_r = workbook.sheet_by_name('enterprise')
    base_urls = sheet_r.col_values(0)
    return base_urls


#爬取企业详情
def get_detail(base_urls,proxys,book,sheet):
    index = 0
    print (type(base_urls))

    for url in base_urls:
        print (url)
        s = requests.get(url,proxies=random.choice(proxys))
        soup = BeautifulSoup(s.text,'lxml')
        try:
            name = soup.select('.gsinfocon > ul > .gslir > span')[0].text
            details = soup.select('.gslxcon > ul')
            address = details[0].select('li')[1].text
            person = details[3].select('li')[1].text
            phone = details[4].select('li')[1].text
            if len(person) >=2:
                sheet.write(index,0,name)
                sheet.write(index,1,person)
                sheet.write(index,2,phone)
                sheet.write(index,3,address)
                index = index + 1
                print ('第%s条爬虫' % index)
        except Exception as e:
            print (e)

if __name__ == "__main__":
    book = xlwt.Workbook()
    sheet = book.add_sheet('enterprise')
    proxys = proxies()
    base_urls = read_url()
    get_detail(base_urls,proxys,book,sheet)
    book.save('./2.xls')
    
    