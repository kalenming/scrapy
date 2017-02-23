# -*- coding: utf-8 -*-
import requests
from bs4 import  BeautifulSoup
import urllib.request
import time
from multiprocessing.dummy import Pool as ThreadPool

def download(url):
    print (url)
    s = requests.get(url)
    # s.encoding = 'urf-8'
    soup = BeautifulSoup(s.text,'lxml')
    pics = soup.select('.wp-item')
    for pic in pics:
        url = pic.select('div > div > a > img')[0].get('src')
        name = pic.select('div > h3 > a')[0].text
        opener=urllib.request.build_opener()
        print ('解析成功！')
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36')]
        urllib.request.install_opener(opener)
        text = "C:\\Users\\Administrator\\Desktop\\meizi\\pic\\" + name + '.jpg'
        try:
				
            print ('下载图片成功！')
        except:
            continue

if __name__ == "__main__":
    urls = ['http://www.meizitu.com/a/list_1_{}.html' .format(str(i)) for i in range(1,20,1)]
    i = "CO"
    if i == 'CON':
        start =  time.clock()
        for url in urls:
            download(url)
            end = time.clock()
            print ('爬虫用时：%s s' % (end-start))
    else:
        start =  time.clock()
        pool = ThreadPool(4)
        results = pool.map(download, urls)
        pool.close()
        pool.join()
        end = time.clock()
        print ('爬虫用时：%s s' % (end-start))