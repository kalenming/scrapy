# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:15:46 2016

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup

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
    url = "http://dota.uuu9.com/201009/65466.shtml"
    url2 = "http://dota.uuu9.com/201009/65466_2.shtml"
    get_result1(url)
    get_result2(url2)