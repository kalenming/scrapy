# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import xlwt

def get_one_page(offset):
    url = 'http://maoyan.com/board/4?offset=%d' % offset
    try:
        s = requests.get(url)
        if s.status_code == 200:
            return s.text
        return None
    except RequestException :
        return None

def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    titles = soup.select('.board-wrapper dd')
    global j
    for t in titles:
        index = t.select('i')[0].text
        name = t.select('a')[0].get('title')
        actor = t.select('.star')[0].text
        time = t.select('.releasetime')[0].text
        score = ''
        scores = t.select('.score i')
        for s in scores:
            score = score + s.text
        sheet.write(j,0,index)
        sheet.write(j,1,name)
        sheet.write(j,2,actor)
        sheet.write(j,3,time)
        sheet.write(j,4,score)
        j = j + 1
        print (j)



def main(offset):
    html = get_one_page(offset)
    parse_one_page(html)



if __name__ == "__main__":
    book = xlwt.Workbook()
    sheet = book.add_sheet('2')
    j = 0
    for i in range(0,10):
        main(i*10)
    book.save('rank.xls')