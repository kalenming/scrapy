# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:49:16 2016

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup

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
        sex = soup.select('.member_pic div')[0].text
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
    return home         
    

        
        
        
    
if __name__ == "__main__":
    data = get_url()
    get_info(data)    