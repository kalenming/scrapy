# -*- coding: utf-8 -*-
import os 
import re
import urllib.request
os.chdir(r'C:\\Users\\Administrator\\Desktop\\')
opener=urllib.request.build_opener()
# print ('½âÎö³É¹¦£¡')
opener.addheaders=[('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36')]
urllib.request.install_opener(opener)
dir = 'C:\\Users\\Administrator\\Desktop\\pic\\'
i = 1
j = 1
with open("detail.txt","rb") as f: 
    os.chdir(dir)
    data = f.read()
    companys = re.findall(r'\[(.*?)\]',str(data))
    for comp in companys:
        urls = re.findall(r'picUrl":"(.*?)"',company)
        os.mkdir(str(i))
        for url in urls:
            url = 'https://www.ljlpay.com/upload/lanjinling/online/' + url
            print (url)
            name = dir + str(i) + '\\' + str(j) + '.jpg'
            urllib.request.urlretrieve(url,name)
            j = j + 1
        i = i + 1