# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:10:15 2017

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

def search_company(cols):
    start = time.clock()
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36"
    )
    
    for col in cols:
        url = 'http://www.tianyancha.com/search?key={}&checkFrom=searchBox' .format(col)
        print (url)
        browser = webdriver.PhantomJS(desired_capabilities=dcap)
        browser.get(url)
        time.sleep(3)
        #find_url = browser.find_element_by_class_name('ng-binding')
        soup = BeautifulSoup(browser.page_source,'lxml')
        browser.quit()
        try:
            find_url = soup.select('.query_name')
            print (find_url)
            com_url = find_url[0].get('href')
            print (col)
            end = time.clock()
            print ('搜索公司用时：%f s' % (end - start))
            data = {'url':com_url,
                    'company':col
                    }    		
            company_url.insert_one(data)
        except  Exception as e: 
            print ('can not find this company in tianyancha!')
    		#d_url = 'http://www.tianyancha.com/company/2347423402'
            #return col,d_url
	
'''def get_result(col,url):
    start = time.clock()
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36"
    )

    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.get(url)
    #print (driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.implicitly_wait(10)
    driver.quit()

    
    try:
        inv = soup.select('#nav-main-outInvestment .m-plele')
        print (len(inv))
        for i in inv:
            print (i)
            inv = i.select('div')
            companyName = inv[0].text
            legalPerson = inv[2].text
            industry = inv[3].text
            state = inv[4].text
            invest = inv[5].text
    
            data = {
            'company':col,
            'enterprise_name': companyName,
            'legal_person_name': legalPerson,
            'industry': industry,
            'status': state,
            'reg_captial': invest
            }
            company.insert_one(data)
            print (data)
    except Exception as e:   
            print ("no invest!")
    end = time.clock()
    print ("获取详情用时:%f s" % (end-start))
'''
def read_xlsx():
    fname = "C:\\Users\\Administrator\\Desktop\\test.xlsx"
    workbook = xlrd.open_workbook(fname)
    sheet = workbook.sheet_by_name('Sheet1')
    cols = sheet.col_values(0)
        #start = time.clock()
    search_company(cols)
        #get_result(col,url)
        #end = time.clock()
        #print ("查询企业用时：%f s" % (end-start))
		#print (time.clock())

if __name__ == "__main__":
    con = pymongo.MongoClient('localhost',27017)#打开数据库端
    db = con.tyc   #这里建立一个库,怎样直接在已有库下面建表还未解决
    company_url = db.company_url    
    read_xlsx()