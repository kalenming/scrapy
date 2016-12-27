# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 10:48:10 2016
@author: guohuaiqi
"""
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from bs4 import BeautifulSoup
import requests
import time

urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,25,25)]
#url='https://movie.douban.com/mine?status=wish'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
    'Cookie':'bid="+RZMojI+I84"; ll="118281"; viewed="7056708_10863574_26647176_3288908"; gr_user_id=7758d24b-1ff7-4bfb-aac5-da0cebb3b129; _ga=GA1.2.1164329915.1430920272; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1457141967%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DwlFfuGH8nDDaDfhuElvs2e-927672lPlTf3UP5ra2LVTDrCK1YcFpyYiIAPJcOqq%26wd%3D%26eqid%3D86da232a00235c820000000356da38c0%22%5D; ps=y; ue="alovera@sina.com"; dbcl2="61719891:SKQE4SmJJ7U"; ck="WzE9"; ap=1; push_noty_num=0; push_doumail_num=0; __utma=30149280.1164329915.1430920272.1457093782.1457141968.44; __utmb=30149280.6.10.1457141968; __utmc=30149280; __utmz=30149280.1457141968.44.23.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.6171; __utma=223695111.1164329915.1430920272.1457093782.1457141968.6; __utmb=223695111.0.10.1457141968; __utmc=223695111; __utmz=223695111.1457141968.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=051573cd37c5bc0e.1446452093.6.1457142204.1457093853.; _pk_ses.100001.4cf6=*'
}

title=[]
image=[]
actor=[]
empression=[]
rate=[]
evalu_num=[]
#爬取并显示top250电影的名称，图片地址，演员等
def allfilm(web_url,data=None):    
    web_data=requests.get(web_url)
    soup=BeautifulSoup(web_data.text,'lxml')
    time.sleep(2)
    titles=soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a')
    images=soup.select('#content > div > div.article > ol > li > div > div.pic > a > img')
    actors=soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > p:nth-of-type(1)')
    empressions=soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > p:nth-of-type(2)')
    rates=soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > div > span.rating_num')
    evalu_nums=soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > div > span:nth-of-type(4)')
    
    print(titles)
    for title1,image1,actor1,empression1,rate1,evalu_num1 in zip(titles,images,actors,empressions,rates,evalu_nums):
        title.append(title1.get_text().replace('\\xa0',' ').strip()),
        image.append(image1.get('src')),
        actor.append(actor1.get_text().replace('\\xa0',' ').strip()),
        empression.append(empression1.get_text()),
        rate.append(rate1.get_text()),
        evalu_num.append(evalu_num1.get_text())

for sigle_url in urls:
    allfilm(sigle_url)
data={'电影名':title,
      '图片链接':image,
      '演员':actor,
      '印象':empression,
      '评分':rate,
      '评价数':evalu_num}        
frame=DataFrame(data,columns=[u'电影名',u'图片链接',u'演员',u'印象',u'评分',u'评价数'])
print('done!!')

#将dataframe数据写入csv或xlsx文件
frame.to_csv('C:/Users/Administrator/Desktop/scrapy/1.csv', decode='gb2312', index=True)