# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import re
import time
import xlwt
def init(url):
    firefox_login=webdriver.PhantomJS()
    firefox_login.get(url)
    firefox_login.maximize_window()
    return firefox_login

# 登录淘宝并进行商品搜索
def login(firefox_login):
    firefox_login.find_element_by_id('J_Quick2Static').click()
    firefox_login.find_element_by_id('TPL_username_1').clear()
    firefox_login.find_element_by_id('TPL_username_1').send_keys(u'淘客先生9')
    firefox_login.find_element_by_id('TPL_password_1').clear()
    firefox_login.find_element_by_id('TPL_password_1').send_keys(u'sdef509')
    a=firefox_login.find_element_by_id('J_SubmitStatic')
    a.click()
    time.sleep(random.randint(6,8))
    firefox_login.find_element_by_id('q').clear()
    firefox_login.find_element_by_id('q').send_keys(u'魅族mx6')
    firefox_login.find_element_by_class_name("btn-search").click()
    time.sleep(random.randint(5,8))
    firefox_login.find_element_by_xpath('//a[@traceidx="0"]').click()
    return firefox_login

if __name__ == "__main__":
    Infolist = []
    url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
    firefox_login = init(url)
    firefox_login = login(firefox_login)
