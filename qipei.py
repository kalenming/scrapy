# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 16:02:20 2017

@author: Administrator
"""

import requests
from bs4 import  BeautifulSoup
import xlwt
from time import sleep
import pymongo

def get_url():
    start_url = 'http://b2b.huangye88.com/qiye/qipei/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    s = requests.get(start_url,headers = headers)
    soup = BeautifulSoup(s.text,'lxml')
    url0 = soup.select('.ad_list')[0]
    url = url0.select('a')
    url_list = list()
    for ur in url:
         url_list.append(ur.get('href'))
    return url_list
    
def get_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    s = requests.session()
    r = s.get(url,headers = headers,timeout=None)
    s.keep_alive = False
    soup = BeautifulSoup(r.text,'lxml')
    page =  int(int(soup.select('.tit span em')[0].text) / 20) + 1
    url_p = ['{}pn{}/'.format(url,str(i)) for i in range(1,page+1)]
    for url_t in url_p:
        get_total(url_t)
        
def get_total(url_t):
    print (url_t)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    s = requests.session()
    r = s.get(url_t,headers = headers,timeout=None)
    s.keep_alive = False
    soup = BeautifulSoup(r.text,'lxml')
    try:
        u1 = soup.select('.main730 .box')[1]
    except Exception as e:  
        print (Exception,":",e)
    
    try:
        u2 = u1.select('.mach_list2 form dl')
        for u3 in u2:
            try:
                u4 = u3.select('dt')
            except Exception as e:   
                print (Exception,":",e)
            if u4:
                try:
                    u = u4[0].select('h4 a')[0].get('href')
                    url_total.append(u)
                    global I
                    print ('第%s个url'%I)
                    I = I + 1
                    get_detail(u)
                except Exception as e:   
                    print (Exception,":",e)
    except Exception as e:   
        print (Exception,":",e)
    
            
            
    return url_total
    
def get_detail(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    s = requests.get(url,headers = headers,timeout=None)
    soup = BeautifulSoup(s.text,'lxml')
    data = soup.select('.c-left .l-txt li')
    if data:
        name.append(data[0].text)
        type.append(data[1].text)
        product.append(data[2].text)
        address.append(data[3].text)
        person.append(data[6].text)
        phone.append(data[8].text)
        data = {
        'name':data[0].text,
        'type':data[1].text,
        'product':data[2].text,
        'address':data[3].text,
        'person':data[6].text,
        'phone':data[8].text
        }
        print (data)
        qiye.insert_one(data)
        global J
        print ('第%s个公司'%J)
        J = J + 1
    

def write_excel(name,type,product,address,person,phone):
    book = xlwt.Workbook()
    ws = book.add_sheet(sheet_name)
    ws.write(0,0,'名称')
    ws.write(0,1,'类型')
    ws.write(0,2,'产品')
    ws.write(0,3,'地址')
    ws.write(0,4,'人')
    ws.write(0,5,'电话')
    for i in range(0,len(name)):
        ws.write(i+1,0,name[i])
        ws.write(i+1,1,type[i])
        ws.write(i+1,2,product[i])
        ws.write(i+1,3,address[i])
        ws.write(i+1,4,person[i])
        ws.write(i+1,5,phone[i])
    book.save('./name.xls')

         
if __name__ == "__main__":
    con = pymongo.MongoClient('localhost',27017)#打开数据库端
    db = con.qipei   #这里建立一个库,怎样直接在已有库下面建表还未解决
    qiye = db.qiye
    I = 0   #用于计数
    J = 0   #用于计数
    url_pro = list()  #省份列表
    url_page = list()  #页列表
    name = list()
    type = list()
    product = list()
    address = list()
    person = list()
    phone = list()
    url_pro = get_url()
    print (len(url_pro))
    url_total = list()
    for url in url_pro:
        get_page(url)
    write_excel(name,type,product,address,person,phone)
    
        