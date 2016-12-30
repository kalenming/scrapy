# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 16:55:22 2016

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup

def get_url():
    host = 'http://bj.58.com'
    right = '?PGTID=0d200005-0000-1ec1-ec5d-8c6575c2970e&ClickID=1'
    web_url = 'http://bj.58.com/sale.shtml'
    
    url = list()  #url列表
    ganji = requests.get(web_url)
    soup = BeautifulSoup(ganji.text,'lxml')
    all_url = soup.select('#ymenu-side > ul > li > ul > li > b > a')
    for item in all_url:
        ur = host + item.get('href') 
        url.append(ur)
    return ur
    
def get_list(url,page):
    page_list='{}pn{}/'.format(cate_url,str(page))
    web_data=requests.get(page_list)
    soup=BeautifulSoup(web_data.text,'lxml')
    if soup.find('td','t'):
        allurl=soup.select('td.t a.t')
        for url1 in allurl:
            content_link=url1.get('href')
            if 'bj.58.com' not in content_link:
                pass
            else:
                urllist.insert_one({'url':content_link})
                # print(content_link)
                get_item_content(content_link)
    else:
        pass  
    
def get_info(url):
    info = requests.get(url)
    soup = BeautifulSoup(info.text,'lxml')
    
    
if __name__ == "__main__":
    url = get_url()
    print (len(url))