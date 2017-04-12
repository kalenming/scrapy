# -*- coding: utf-8 -*-
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import json
import os
from hashlib import md5
import time
from multiprocessing.dummy import Pool as ThreadPool


#请求索引页
def get_index_page(page):
    url = 'http://www.toutiao.com/search_content/?offset=%s&format=json&keyword=街拍&autoload=true&count=20&cur_tab=1' % page
    try:
        s = requests.get(url)
        if s.status_code == 200:
            return s.text
        return None
    except RequestException:
        print ('请求索引页出错',url)
        return None

#解析索引页
def parse_index_page(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

#获取详情页
def get_detail_page(url):
    try:
        s = requests.get(url)
        if s.status_code == 200:
            return s.text
        return None
    except RequestException:
        print ('获取详情页失败',url)
        return None
#解析详情页
def parse_detail_page(html,url):
    soup = BeautifulSoup(html,'html.parser')
    #title = soup.select('.article-title')[0].text
    imgurls = soup.select('.article-content p')
    imgs = list()
    for im in imgurls:
        try:
            imgurl = im.select('img')[0].get('src')
            imgs.append(imgurl)
        except Exception as e:
            print (e)
    for img in imgs:
        download_img(img)

#下载图片
def download_img(img):
    s = requests.get(img)
    if s.status_code == 200:
        save_img(s.content)
#保存图片
def save_img(content):
    filepath =  '{0}\{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os._exists(filepath):
        with open(filepath,'wb') as f:
            f.write(content)
            f.close()




def main(page):
    html = get_index_page(page)
    urls = parse_index_page(html)
    for url in urls:
        html = get_detail_page(url)
        res = parse_detail_page(html,url)



if __name__ == "__main__":
    # start = time.clock()
    # pool = ThreadPool(4)
    # group = [page*20 for page in range(0,5)]
    # results = pool.map(main,group)
    # pool.close()
    # pool.join()
    # end = time.clock()
    # print('多线程用时%s' % (end-start))

    start = time.clock()
    main(0)
    end = time.clock()
    print('单线程用时%s' % (end - start))
