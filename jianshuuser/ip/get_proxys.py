import requests
import os
from bs4 import BeautifulSoup
os.chdir(r'C:\Users\Administrator\Desktop\scrapy\scrapy\jianshuuser\ip')
import random

def get_proxies():
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    base_url = 'http://www.xicidaili.com/wt/'
    fp = open('host.txt','w')
    for p in range(1,2):
        url = base_url + str(p)
        s = requests.get(url,headers = headers)
        soup = BeautifulSoup(s.text,'lxml')
        ips = soup.select('#ip_list tr')
        
        for i in ips:
            try:
                ipp = i.select('td')
                ip = ipp[1].text
                host = ipp[2].text
                fp.write(ip)
                fp.write(':')
                fp.write(host)
                fp.write('\n')
            except Exception as e :
                print ('no ip !')
    fp.close()

def check_proxies():
    # headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    url = 'https://www.baidu.com/'
    fp = open('host.txt','r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        proxy =p.strip('\n')
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