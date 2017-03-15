# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:36:37 2017

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup

def cookie_login():
    data = {
    'Accept':'text/html, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'remember_user_token=W1sxNTI1MTMwXSwiJDJhJDEwJEYvTTNWYmcvbnQ1TlZFQWVoT29uOGUiLCIxNDg4OTQ1NDc2LjAzOTk3MSJd--4be8b3cf52db32a39b15edd34a880243bb3aa0ea; CNZZDATA1258679142=1094691586-1488943605-%7C1489105668; _ga=GA1.2.1142387018.1488945470; _gat=1; _session_id=MmROZVlGaHdVajU0cEVhZUFUNDU0UG5iOUQxZzQ3YVBkWi9qN2cwOEttc1l1T0U4Y3lxaE1UVU9LTjJPSUgwSFJ5Z1lJaDR3UkNkL3hWNTMwWGdyZkhia0RoSEJoeXAzNTh6WE1wSFdNeHpnSE9yM0NpSGNreXBZWFBDbkNoZU5XelU4TDNGUEtXVWpDdGVDR3FrKzQyWE1QSStTT1F3RXJKa3FFeUlwSDFKaytQNnAxM3hsRjBqbXVjbTJ6QVFpdFlyOHBsT0RoZXVQcHBQSmRTemNqN1JWYU4vdnFzdlpuR1FJN3JLeTFyNEJ2SjRRWkxTREN2TFNRR2RoeWg3MEF3OG44SjB0bnFoaHdNTGNDN1QvYXFQMDU1Zkh1LytrWWYzZjVVZEE5Y2U5UXFJWXRSWm9DcnRnWGYybXhXWUxtd2wvK0xtOVFEMUJXam0wbkpETHg1ejM3M3Fab21iaEp1dVBaMDI5a3hnY1pjNlh1MXJWdk5JY3k5aTNkWGNlRURlY0lZbmkwTDQvelNKY21uMmlXTEFXNGQxdHN2eCs4bmRmbHJzYndPaz0tLXFyU2M4bGRWRDhxSzZZUi9kR2xSY0E9PQ%3D%3D--75d2c35d51588b280596090caa0863f32e8e47d4',
    'Host':'www.jianshu.com',
    'Referer':'http://www.jianshu.com/users/yZq3ZV/followers?page=3610',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'X-CSRF-Token':'RfJm8Gh1ax+0+p2vV4YGazj8oZ9E80kOQeGd1fh1UgKpTrt+6t3kvdYRHH/l4XPDhy4tQ0qNiey5Wo6hoj3t2w==',
    'X-INFINITESCROLL':'true',
    'X-Requested-With':'XMLHttpRequest'   
    }
    base_url = "http://www.jianshu.com/users/yZq3ZV/followers?page="
    for i in range(1,2):
        url = base_url + str(i)
        print (url)
        s = requests.get(url,cookies = data)
        soup = BeautifulSoup(s.text,'lxml')
        print (soup)
    

if __name__ == "__main__":
    cookie_login()
    
