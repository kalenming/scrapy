# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import xlwt
import time
from multiprocessing.dummy import Pool as ThreadPool

#获取爬虫列表
def get_url():
    start_url = 'http://www.autozi.com/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    s = requests.get(start_url,headers = headers)
    soup = BeautifulSoup(s.text,'lxml')
    url_list = list()
    url = soup.select('.subMenu-title a')
    for ur in url:
        url_list.append(ur.get('href'))
    print (len(url_list))
    return url_list
    
def get_detail(url):
   
    print (url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    s = requests.get(url,headers = headers)
    soup = BeautifulSoup(s.text,'lxml')
    r =  int(s.status_code)
    if 200 == r:
    
        if 'currentPageNo' not in url:
            total = soup.select('.page-btn')[0].get('onclick').split(',')[4][1:-1]
            for i in range(1,int(total)):
                url_each = url + '&currentPageNo=' + str(i)
                get_detail(url_each)
    
        else:
            name = soup.select('.list-name  h4 a')
            item = soup.select('.event-a span')
            if item:
                global I
                for na in name:
                    print ('第%s条:'%I)
                    names.append(na.text)
                    items.append(item[0].text)
                    I = I+1
    return names,items

#保存文件

def write_excel(book,sheet_name,names,items):
    ws = book.add_sheet(sheet_name)
    ws.write(0,0,'名称')
    ws.write(0,1,'分类')

    for i in range(0,len(names)):
        ws.write(i+1,0,names[i])
        ws.write(i+1,1,items[i])
    book.save('./zc.xls')
            
if __name__ == "__main__":
    book = xlwt.Workbook()  
    names = list() #名称
    brands = list() #品牌
    items = list() #分类
    I = 1
    J = 1
    start_time = time.time()
    url_list = get_url()
    

    pool = ThreadPool(4)

    pool.map(get_detail,url_list)
    pool.close()
    pool.join()
    sheet_name = '1'
    write_excel(book,sheet_name,names,items)
    end_time = time.time()
    print ('耗时：%s'%(end_time-start_time))