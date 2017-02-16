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
    print (len(url))
    return url




def get_list(url):
    for each_url in url:
        
        page_list=each_url + 'pn1/?PGTID=0d3001f0-0000-124b-323d-1d19986bf478&ClickID=1'
        print (page_list)        
        web_data=requests.get(page_list)
        soup=BeautifulSoup(web_data.text,'lxml')
        data = list()
        
        allurl=soup.select('#infolist > div.infocon > table > tbody > tr > td.t > a')
        for url1 in allurl:
            content_link=url1.get('href')
            data.append(content_link)
        
    print (len(data))
    return data
    
    
# 爬取每个页面的详情内容,包括标题，时间，价格，区域
def get_item_content(content_link):
# 先判断数据是否来自58，将来自精品或者转转的数据，统一不要
    for url2 in content_link:
        print (url2)
        web_data1=requests.get(url2)
        soup=BeautifulSoup(web_data1.text,'lxml')
        page_not_exist = '404' in soup.find('script',type='text/javascript').get('src').split('/')
        #body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span        
        if page_not_exist:
            pass
        else:
            if '区域' in soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_tit')[0].get_text():
                if soup.find_all('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span'):
                    district=list(soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span')[0].stripped_strings)
                else:
                    district=list(soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con')[0].stripped_strings)
            elif '区域' in soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_tit')[0].get_text():
                if soup.find_all('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span'):
                    district=list(soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span')[0].stripped_strings)
                else:
                    district=list(soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con')[0].stripped_strings)
            else:
                district=None
            data={
                'goods_cate':soup.select('#header > div.breadCrumb.f12 > span:nth-of-type(3) > a')[0].text.strip(),
                'title':soup.select('#content h1')[0].text.strip(),
                'date':soup.select('#content li.time')[0].text.replace('.','-'),
                'price':soup.select('span.price.c_f50')[0].text.replace('元','').strip() if '面议'not in soup.select('span.price.c_f50')[0].text else None,
                'district':district
                }
            #content.insert_one(data)
            # print(data)
            detail.append(data)
    return detail
    
if __name__ == "__main__":
    detail = list()
    url = get_url()
    data = get_list(url)
    detail = get_item_content(data)
    print (detail)