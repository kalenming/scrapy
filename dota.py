# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:15:46 2016

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup




    

def get_url():
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'bdshare_firstime=1483066981240; JBU1_fa5e_saltkey=jJ08RBMz; JBU1_fa5e_lastvisit=1483063453; CNZZDATA4419939=cnzz_eid%3D802704931-1483067482-%26ntime%3D1483078649; CNZZDATA30026049=cnzz_eid%3D165501596-1483066744-%26ntime%3D1483078778; CNZZDATA156663=cnzz_eid%3D959010333-1483064083-%26ntime%3D1483074890; CNZZDATA30012669=cnzz_eid%3D1519255423-1483066908-%26ntime%3D1483077777; djfccookie=foo; CNZZDATA4996648=cnzz_eid%3D532931981-1483065900-http%253A%252F%252Fdota.uuu9.com%252F%26ntime%3D1483162613; Hm_lvt_7915c7f3a0b7fa088fba9f6967470bee=1483067083,1483163989; Hm_lpvt_7915c7f3a0b7fa088fba9f6967470bee=1483164714; rmgH_fa5e_saltkey=qVgEFgJV; rmgH_fa5e_lastvisit=1483162016; rmgH_fa5e_ulastactivity=8f69zFvb1KAwTO1uLw3yb2412%2BQ9uDHnaUW0hIaNr2qASuUegXdO; rmgH_fa5e_creditnotice=0D5D0D2D0D0D0D1D0D13169420; rmgH_fa5e_creditbase=0D10D0D0D5D0D0D0D0; rmgH_fa5e_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; rmgH_fa5e_mashine_killer=7411VHoe6d92n8EyQ%2FaYYGZQ8bSDSxBnxmcb6MJOghhQrCwkGg; rmgH_fa5e_u9_user=zhiming509%0913169420; rmgH_fa5e_u9_auth=fe22nM77dMBXxEt5qiP8zVKKdHUf%2BxzgSZTSWv8ob7LvUqaLBkfoLYK4Y6Ygo9jD; rmgH_fa5e_sid=H6ZG9z; rmgH_fa5e_lastact=1483167471%09uc.php%09; rmgH_fa5e_auth=c809ZmSuVKyaAnnUoFWiMD9EvBwsyFUTYBejdbRQ6a3NeWOMzxyUmBnqCq8854ehnFRqE%2FZtsq4xf%2BTIUjyXlAz3h2RfIA; JBU1_fa5e_sid=e66prZ; JBU1_fa5e_lastact=1483167471%09uc.php%09; JBU1_fa5e_auth=d90e0BKZSGLNYuBqpsMHd7ygjC9JGbSeUe0KkKb8DQhg6LICF6KfHw0oWSYE22JUBuZz%2FwOdpY%2FcZrJBC7jo16%2Fw7c96jQ; CNZZDATA4996543=cnzz_eid%3D1975976930-1483063932-%26ntime%3D1483165364; tacc=c; CNZZDATA4995947=cnzz_eid%3D788040324-1483064670-%26ntime%3D1483163517; CNZZDATA4990579=cnzz_eid%3D1467950524-1483062298-%26ntime%3D1483164202',
    'Host':'dota.uuu9.com',
    'Referer':'http://u.uuu9.com/logging.php?ac=login',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    dota=requests.get('http://dota.uuu9.com/gl/',headers = headers); #这里是想要抓取页面的地址。
    dota.encoding = 'gb2312'
    soup = BeautifulSoup(dota.text,'lxml')
    url = soup.select('.content ')
    print (len(soup))
    print (soup)
    
def get_result1(url):
    dota = requests.get(url)
    dota.encoding = 'gb2312'
    soup = BeautifulSoup(dota.text,'lxml')

    heros = list()
    hero = soup.select(".Apple-style-span strong")
    heros.append(hero[0].text.replace('\xa0',''))
   
    
def get_result2(url):
    dota = requests.get(url)
    dota.encoding = 'gb2312'
    soup = BeautifulSoup(dota.text,'lxml')
    
    introductions = list()
    introduction = soup.select('#content p')
    for i in introduction:
        introductions.append(i.text.replace('\xa0',''))
    print (introductions)
    
if __name__ == "__main__":
    web_url = 'http://dota.uuu9.com/gl/'
    get_url()