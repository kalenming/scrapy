# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:11:02 2017

@author: Administrator
"""
import requests
from bs4 import  BeautifulSoup
import urllib.request
import xlrd

def dow_pic():
    #读取待下载头像的url
    file = xlrd.open_workbook('all.xls')
    data =  file.sheet_by_name(u'Sheet3')
    urls = data.col_values(0)
    print (len(urls))
    
    data = {
        'Accept:text/html':'application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'pgv_pvi=410030080; pgv_si=s8182293504; webwxuvid=bd6bbe8fbf76abb54e2a391c8279a87a12c62149157763ba2a09ba590f237445a4b1c52e54892207493c0c2a3ca906dc; webwx_auth_ticket=CIsBEKLy2tMGGoABCiWQ+5fyhCqhN+mssCO/XaEZFO7Fl0f1vf4xDiS83Nxkj2I/1C5BogbXtFYdLEV8LPww+z6aoSuXyVaXrY/nMf11UkZyLT6mmzO2DuK2mLqVx6GSwUWAwSxiOiBD7gzDomOLDOXLDNrRU+eSqzQ6GBrg/McvbLrTj2KQ2+7w5uo=; login_frequency=1; last_wxuin=9008695; wxloadtime=1488938400_expired; _qpsvr_localtk=0.3579975199417189; RK=sPvvct3feD; ptcz=49529177af0d7fe0fb88ff3e5653fcea821578f74a46051c8c830d1c83f2f8a6; pt2gguin=o0915840827; uin=o0915840827; skey=@lU0nty9Pb; MM_WX_NOTIFY_STATE=1; MM_WX_SOUND_STATE=1; wxpluginkey=1488934262; wxuin=9008695; wxsid=eAaXev2mpp+dLySs; webwx_data_ticket=gSeebY/2ZG4bDpYCVXWF4DKr; mm_lang=zh_CN',
        'Host':'wx.qq.com',
        'If-Modified-Since':'Wed, 08 Mar 2017 04:02:07 GMT',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    index = 1
    dir =   'C:\\Users\\Administrator\\Desktop\\scrapy\\proxy\\wx\\'
    for url in urls:
        dow_url  =  'https://wx.qq.com' + url
        r = requests.get(dow_url,cookies = data)
        name = dir + str(index) + '.jpg'
        imageContent = (r.content)
        fileImage = open(name, 'wb')
        fileImage.write(imageContent)
        fileImage.close()
        print('正在下载第%d位好友头像'% index)
        index = index + 1
    
if __name__ == "__main__":
    dow_pic()