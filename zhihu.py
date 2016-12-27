# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import re

headers={'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 5.1;zh-CN;rv:1.9.2.9)Gecko/20100824 Firefox/3.6.9'}
data = {'form_email':'915840827@qq.com',
          'form_password':'sdef031',
          'redir':    'https://www.douban.com',
          'login':u'登陆'
          }
loginUrl = 'http://www.douban.com/accounts/login'
r = requests.post(loginUrl,data = data,headers = headers)
page = r.text
# print r.url

'''''获取验证码图片'''
# 利用bs4获取captcha地址
soup = BeautifulSoup(page, "html.parser")
captchaAddr = soup.find('img', id='captcha_image')['src']
# 利用正则表达式获取captcha的ID
reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
captchaID = re.findall(reCaptchaID, page)
# print captchaID
# 保存到本地
urllib.urlretrieve(captchaAddr, "captcha.jpg")
captcha = raw_input('please input the captcha:')
data['captcha-solution'] = captcha
data['captcha-id'] = captchaID
r = requests.post(loginUrl,data=data,headers=headers)
page = r.text
print page