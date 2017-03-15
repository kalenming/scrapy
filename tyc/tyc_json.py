# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:45:42 2017

@author: Administrator
"""

#coding:utf-8
from selenium.webdriver.common.keys import Keys  
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pymongo
import xlrd
import time 
from bs4 import  BeautifulSoup
import requests
import time
import re
import json
import random


def search_company_person():


    proxys = ['119.5.0.119:808','111.155.116.202:8123','121.31.149.168:8123','202.108.2.42:80',
             '175.155.24.25:808','106.46.136.215:808' ]
    
    session = requests.session()
    session.cookies.set("tnet", "218.108.215.127")
    #start_url = 'http://www.tianyancha.com/search/or'
    start_url = "http://www.tianyancha.com/company/2316265706"
    
    #invests = ['or0100','or100200','or200500','or5001000','or1000']
    #years = ['-e01','-e015','-e510','-e1015','-e15']
    #start = 1000
    #end = 200000
    for p in range(1,20):
        #index_url = start_url + str(start) + str(end)  + '/p{}?key=%E6%B1%BD%E9%85%8D'.format(str(p))
        index_url = start_url
        tongji_url = "http://www.tianyancha.com/tongji/2316265706.json?random=%d" % int(time.time()) * 1000
        api_url = "http://www.tianyancha.com/expanse/inverst.json?id=2316265706&ps=20&pn=1"
    
        public_headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"
        }
        api_headers = public_headers.copy()
        api_headers.update({
            "Tyc-From": "normal",
            "Accept": "application/json, text/plain, */*",
            "Referer": index_url,
            "Accept-Encoding":"gzip, deflate, sdch"
        })
        index_page = session.request("GET", index_url, headers = public_headers)
    
        soup = BeautifulSoup(index_page.text,'lxml')
        js_url = soup.select('script')[4].get('src')
        print (js_url)
    
        js_page = session.request("GET", js_url, headers = public_headers)
        # soup = BeautifulSoup(js_page.text,'lxml')
    
        sgattrs = json.loads(re.findall(r"n\._sgArr=(.+?);", str(js_page.content))[0])
        print (sgattrs)
    
        try:
            tongji_page = session.request("GET", tongji_url, headers = api_headers)
            print (tongji_page.content)
            js_code = "".join([ chr(int(code)) for code in tongji_page.json()["data"]["v"].split(",") ])
            token = re.findall(r"token=(\w+);", js_code)[0]
            print("token:", token)
        
            fxck_chars = re.findall(r"\'([\d\,]+)\'", js_code)[0].split(",")
            sogou = sgattrs[9] # window.$SoGou$ = window._sgArr[9]
            utm = "".join([sogou[int(fxck)] for fxck in fxck_chars])    # if(window.wtf){var fxck = window.wtf().split(",");var fxckStr = "";for(var i=0;i<fxck.length;i++){fxckStr+=window.$SoGou$[fxck[i]];}document.cookie = "_utm="+fxckStr+";path=/;";window.wtf = null;}
            print("utm:", utm)
        
            session.cookies.set("token", token)
            session.cookies.set("_utm", utm)
        
            r = session.request("GET", api_url, 
                headers = api_headers)
                
            #company_person.insert_one(r.json())
            #time.sleep(10)
            print (r.json())
        except Exception as e:
            print (e)
if __name__ == "__main__":
    #con = pymongo.MongoClient('localhost',27017)#打开数据库端
    #db = con.tyc   #这里建立一个库,怎样直接在已有库下面建表还未解决
    #company_person = db.company_person    
    search_company_person()