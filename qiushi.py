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

urls=['http://www.qiushibaike.com/hot/page/{}/?s=4942752'.format(str(i)) for i in range(1,3,1)]
#url='https://movie.douban.com/mine?status=wish'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'_xsrf=2|de05d702|4bd90624827119dd0b4ffadd44e59667|1482825706; _qqq_uuid_="2|1:0|10:1482825706|10:_qqq_uuid_|56:YjcyYzI2MmM0MjY4Y2I1MjVhMGQxMzgwNTRhOTM0NjA2NzA3ZDJjYQ==|f10a5dc96c6bb5eb4e8f2141c616a57aa64be889aae4440e031b8038aa145289"; afpCT=1; _gat=1; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1481371732,1481373557,1481437471,1482825708; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1482825731; _ga=GA1.2.323694707.1482825711'
    }

title=[]    
support = []
content = []
#爬取并显示top250电影的名称，图片地址，演员等
def allfilm(web_url,data=None):
    web_data=requests.get(web_url)
    soup=BeautifulSoup(web_data.text,'lxml')
    time.sleep(2)
    titles = soup.select('#content > div > div.col1 > div > div.author > a')
    #supports = soup.select('#content > div > div >div > div.status >span.stats-vote > i.number')
    contents = soup.select('#content > div > div.col1 > div > a > div > span')
    print (titles)
    print(contents)
    for title1,content1  in zip(titles,contents):
        title.append(title1.get_text())
        #support.append(support1)
        content.append(content1.get_text())

for sigle_url in urls:
    allfilm(sigle_url)
data={'标题':title,
      '内容':content,
      }
frame=DataFrame(data,columns=[u'标题',u'内容'])
print('done!!')

#将dataframe数据写入csv或xlsx文件
frame.to_csv('C:/Users/Administrator/Desktop/scrapy/2.csv', decode='gb2312', index=True)

