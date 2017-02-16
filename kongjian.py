# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:13:47 2017

@author: Administrator
"""

# !/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'guohuaiqi'

import requests
from bs4 import BeautifulSoup

url='http://user.qzone.qq.com/915840827/infocenter?ptsig=GM4grvjZzY5QBOeCsEe1t4TMolZAXVc8ZBiR2ZRArIg_'
headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'pac_uid=1_915840827; tvfe_boss_uuid=de0b2aadbb7b31fa; __Q_w_s_hat_seed=1; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s__appDataSeed=1; luin=o0915840827; lskey=0001000047db2cf361dc5aa78a3bca641f8f009a3d8b513b45942d87a5c375671891f10ef7f2490de43bce6c; randomSeed=769976; pgv_pvid=9609630914; o_cookie=915840827; ptisp=ctc; RK=sPvvdt3feB; pgv_info=ssid=s6503784578; pt2gguin=o0915840827; uin=o0915840827; skey=@r9t683cM0; ptcz=7f8d8c322ed4aaa05ae4a686d97f7e28ea898a50d749b31eeca39ca22daf13b7; Loading=Yes; qzspeedup=sdch; p_skey=IZU5yLHQXph8gei4NPtGdNaG2fAluJjGpBfJxCXzIS0_; p_uin=o0915840827; pt4_token=kG0PJMIVdl7egNFRq6*2HSyycXN1TsooBf-Qig8DpG8_; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=4',
        'Host':'user.qzone.qq.com',
        'If-Modified-Since':'Tue, 03 Jan 2017 06:14:28 GMT',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
       }

web_data=requests.get(url,headers=headers)
soup=BeautifulSoup(web_data.text,'lxml')
shuoshuo=soup.select('#menuContainer > div > ul > li.menu_item_311 > a')[0].get_text()
href=soup.select('#menuContainer > div > ul > li.menu_item_311 > a')[0].get('href')
print(shuoshuo,href)