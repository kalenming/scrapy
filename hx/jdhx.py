# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:48:29 2017

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import xlwt
import re 

#获取类别url
def get_category():
    #cookies
    data = {
        'Referer':'https://fresh.jd.com/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    
    #海鲜水产页面
    base_url = "https://list.jd.com/list.html?cat=12218%2C12222&go=0"
    s = requests.get(base_url,cookies = data)
    soup = BeautifulSoup(s.text,'lxml')
    #分类页面
    categorys = soup.find(class_ = 'J_valueList v-fixed')
    
    urls = list()
    
    #遍历分类
    for c in categorys:
        #获取分类url
        category = 'https://list.jd.com' + c.select('a')[0].get('href')
        urls.append(category)
    return urls
    
def get_detail():
    data = {
        'Referer':'https://fresh.jd.com/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    index = 0
    u = "https://list.jd.com/list.html?cat=12218,12222,12242"
    u = "https://list.jd.com/list.html?cat=12218,12222,12243"    
    s = requests.get(u,cookies = data)
    pages = int(int(re.findall(r'<span>(\d+)',s.text)[0]) / 60) + 1
    print ('此页面共有%d页！'% pages)
    for i in range(1,pages+1):        
        url = u + ('&page=%d&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main' % i)
        print (url)
        driver = webdriver.PhantomJS(desired_capabilities={'phantomjs.page.settings.resourceTimeout': '5000'})
        driver.get(url)
        #driver.implicitly_wait(5)
        soup = BeautifulSoup(driver.page_source,'lxml')
        driver.quit()
        titles = soup.select('.gl-item')
        #print (titles)
        for t in titles:
            i = 0
            price = t.find(class_ = "J_price").text
            name = t.select('.p-name > a > em')[0].text
            print ('%s的价格%s' % (name,price))
            sheet.write(index,i,name)
            i = i + 1
            sheet.write(index,i,price)
            index = index + 1
        
if __name__ == "__main__":
    book = xlwt.Workbook()
    sheet = book.add_sheet('1')
    #urls = get_category()
    get_detail()
    book.save('pd3.xls')