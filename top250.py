# -*-encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import xlwt

def get_result(url):
    res = requests.get(url)
    re = BeautifulSoup(res.text,'lxml')
    
    
    title = re.select('#content .hd a ')
    for tit in title:
        ti = tit.select('span')[0]
        titles.append(ti.text)
    director = re.select('#content .bd  ')
    for dir in director:
        d = dir.select('p')[0]
        directors.append(d.text)
    rate = re.select('#content .rating_num')
    for i in rate:
        rates.append(i.text)
    impress = re.select('#content .quote')
    for i in impress:
        impressions.append(i.text)
    return titles,directors,rates,impressions

def write_excel(book,sheet_name,titles,directors,rates,impressions):
    ws = book.add_sheet(sheet_name)
    ws.write(0,0,'电影名')
    ws.write(0,1,'导演')
    ws.write(0,2,'评分')
    ws.write(0,3,'印象')
    for i in range(0,len(impressions)):
        ws.write(i+1,0,titles[i])
        ws.write(i+1,1,directors[i])
        ws.write(i+1,2,rates[i])
        ws.write(i+1,3,impressions[i])
    book.save('./film.xls')
        
        
        
    
    
    
if __name__ == "__main__":
    book = xlwt.Workbook()    
    
    titles = list()
    rates = list()
    directors = list()
    impressions = list()
    web_url = ['https://movie.douban.com/top250?start={}&filter=' .format(str(i)) for i in range(0,250,25)]
    for url in web_url:
        get_result(url)
    print ( len(directors))
    print (len(titles))
    print (len(rates))
    print (len(impressions))
    sheet_name = 'film'
    #write_excel(book,sheet_name,titles,directors,rates,impressions)
    