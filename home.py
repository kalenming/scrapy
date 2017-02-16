# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:49:16 2016

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import pymongo




def get_url():
    web_url = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/' .format(str(i)) for i in range(1,11)]
    
    data = list()    
    for url in web_url:
        home = requests.get(url)
        soup = BeautifulSoup(home.text,'lxml')
        
        ur = soup.select('.pic_list > li > a')
        for u in ur:
            b = u.get('href')
            data.append(b)
        
    return data
    
def get_info(data):
    print (len(data))
    home = list()
    for url in data:
        det = requests.get(url)
        soup = BeautifulSoup(det.text,'lxml')
        title = soup.select('.pho_info h4 em')[0].text
        address = soup.select('.pho_info .pr5')[0].text
        price = soup.select('#pricePart .day_l span')[0].text
        image1 = soup.select('#curBigImage')[0].get('src')
        name =  soup.select('.lorder_name')[0].text
        sex = gender(soup.select('.member_pic')[0].get('class'))
        image2 = soup.select('.member_pic a img')[0].get('src')
        
        
        house = {'title':title,
                 'address':address,
                 'price':price,
                 'sex':sex,
                 'image1':image1,
                 'image2':image2
        }  
        home.append(house)
        print (home)
        house_info.insert_one(house)
    print ('the work has finished!')        
    
def gender(class_name):
    if class_name=='member_ico':
        return 'male'
    else: return 'famale'

        
        
        
    
if __name__ == "__main__":
    client=pymongo.MongoClient('localhost',27017)#打开数据库端
    bnb=client['bnb']#这里建立一个库,怎样直接在已有库下面建表还未解决
    house_info=bnb['house_info']
    data = get_url()
    get_info(data)    