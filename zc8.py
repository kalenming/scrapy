# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import xlwt

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
    
    if 'currentPageNo' not in url:
        total = soup.select('.page-btn')[0].get('onclick').split(',')[4][1:-1]
        for i in range(1,int(total)):
            url_each = url + '&currentPageNo=' + str(i)
            get_detail(url_each)

    else:
        name = soup.select('.list-name  h4 a')
        global I
        global J
        for na in name:
            print ('第%s条:'%I)
            names.append(na.get_text())
            items.append(it[J-1])
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
    book.save('./zc8.xls')
            
if __name__ == "__main__":
    book = xlwt.Workbook()  
    names = list() #名称
    it = ['油品','蓄电池','滤清器','雨刮片','制动系','照明','点火系','轮胎','皮带涨紧轮']
    brands = list() #品牌
    items = list() #分类
    I = 1
    J = 8
    #url_list = get_url()
    url = 'http://www.autozi.com/goods/search.html?_=1457597661681&&&categoryId=140009000000000&categoryLevel=2'
    names,items = get_detail(url)
    sheet_name = '1'
    write_excel(book,sheet_name,names,items)