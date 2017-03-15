# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xlwt
import requests
from bs4 import BeautifulSoup
import random
import os

def proxies():
    os.chdir(r'C:\Users\Administrator\Desktop\scrapy\proxy')
    fp = open('host.txt','r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        proxy =p.strip('\n')
        proxies = {'proxy':proxy}
        proxys.append(proxies)
    return proxys
    


#获取企业url
def get_url(proxys):
    
    os.chdir(r'\Users\Administrator\Desktop\scrapy\scrapy\youboy')
    base_url = 'http://qiye.youboy.com/type/1225_'
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}

    final_urls = set()
    end_urls = list()
    for i in range(0,10000):
        url = base_url + str(i) +'.html#page=' + str(i)
        print (url)
        try:
            s = requests.get(url,proxies=random.choice(proxys),headers = headers,timeout = 1)
            soup = BeautifulSoup(s.text,'lxml')
            des_urls = soup.select('.dqscontit')
            for url in des_urls:
                des_url = url.select('a')[0].get('href')
                des_url = 'http://qiye.youboy.com' + des_url
                final_urls.add(des_url)
                end_urls.append(des_url)
        except Exception as e:
            print (e)
    urls = final_urls
    print (end_urls)
    print (final_urls)
    index = 0
    for url in urls:
        print ('第%d个url' % (index+1))
        sheet.write(index,0,url)
        index = index + 1
        
if __name__ == "__main__":
    book = xlwt.Workbook()
    sheet = book.add_sheet('enterprise')
    proxys = proxies()
    get_url(proxys)
    book.save('./1.xls')