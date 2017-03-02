import requests
import os
from bs4 import BeautifulSoup
os.chdir(r'C:\Users\Administrator\Desktop\scrapy\proxy')
import random

def get_proxies():
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    url = 'http://www.xicidaili.com/nn/1'
    s = requests.get(url,headers = headers)
    soup = BeautifulSoup(s.text,'lxml')
    ips = soup.select('#ip_list tr')
    fp = open('host.txt','w')
    for i in ips:
        try:
            ipp = i.select('td')
            ip = ipp[1].text
            host = ipp[2].text
            fp.write(ip)
            fp.write('\t')
            fp.write(host)
            fp.write('\n')
        except Exception as e :
            print ('no ip !')
    fp.close()

def check_proxies():
    # headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    url = 'http://101.201.82.191:8762/'
    fp = open('host.txt','r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        ip =p.strip('\n').split('\t')
        proxy = 'http://' +  ip[0] + ':' + ip[1]
        proxies = {'proxy':proxy}
        proxys.append(proxies)
    i = random.choice(proxys)
    print (i)
    for pro in proxys:
        try :
            s = requests.get(url,proxies = pro,timeout=5)
            print (s)
        except Exception as e:
            print (e)
            
if __name__ == "__main__":
    get_proxies()
    check_proxies()