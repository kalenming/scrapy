# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:58:53 2017

@author: Administrator
"""

import requests
from bs4 import  BeautifulSoup
import xlwt

def get_contact_json():
    #采用cookies登陆    
    data = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'pgv_pvi=410030080; pgv_si=s8182293504; webwxuvid=bd6bbe8fbf76abb54e2a391c8279a87a12c62149157763ba2a09ba590f237445a4b1c52e54892207493c0c2a3ca906dc; webwx_auth_ticket=CIsBEKLy2tMGGoABCiWQ+5fyhCqhN+mssCO/XaEZFO7Fl0f1vf4xDiS83Nxkj2I/1C5BogbXtFYdLEV8LPww+z6aoSuXyVaXrY/nMf11UkZyLT6mmzO2DuK2mLqVx6GSwUWAwSxiOiBD7gzDomOLDOXLDNrRU+eSqzQ6GBrg/McvbLrTj2KQ2+7w5uo=; login_frequency=1; last_wxuin=9008695; wxloadtime=1488938400_expired; wxpluginkey=1488934262; wxuin=9008695; wxsid=eAaXev2mpp+dLySs; webwx_data_ticket=gSeebY/2ZG4bDpYCVXWF4DKr; mm_lang=zh_CN; MM_WX_NOTIFY_STATE=1; MM_WX_SOUND_STATE=1',
    'Host':'wx.qq.com',
    'Referer':'https://www.baidu.com/link?url=ZcSQmYeMHWlQ7DQPwYormxbDlMhCCuczeNQ86NhiymO&wd=&eqid=c844e40f000e134c0000000358bf6590',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    
    index = 0
    contact_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?r=1488938515070&seq=0&skey=@crypt_48828021_4e8bff905ed9da2d4b28b94bbc72dbdb'
    url = 'https://wx.qq.com/'
    s = requests.get(contact_url,cookies = data)
    flag = list()
    s.encoding = 'utf-8'
    for member in s.json()['MemberList']:
        item = 0 
        #把json里边的所有字段都写到excel里边
        for value in member.values():
            sheet.write(index,item,value)
            item = item + 1
        index = index + 1
    


if __name__ == "__main__":
    book = xlwt.Workbook()
    sheet = book.add_sheet('pic')
    get_contact_json()    
    book.save('./all.xls')
    