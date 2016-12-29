# -*-encoding:utf-8 -*-
import requests
import xlwt
from bs4 import BeautifulSoup



def get_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')


    cont = soup.select('.content')
    auth = soup.select('.author h2')
    for con,aut in zip(cont,auth):
        if con and aut:
            content.append(con.text.split('\n'))
            author.append(aut.text)
    return author,content
    
def write_excel(book,sheet_name,author,content):
     
    sheet = book.add_sheet(sheet_name)
    sheet.write(0,0,'作者')
    sheet.write(0,1,'内容')
    for i in range(len(author)):
        sheet.write(i+1,0,author[i])
        sheet.write(i+1,1,content[i])
    book.save('./qiushi.xls')
    
if __name__ == "__main__":
    book = xlwt.Workbook(encoding='utf-8')
    web_url = ["http://www.qiushibaike.com/8hr/page/{}/?s=4943272" .format(str(i)) for i in range (1,5,1)]
    sheet_name = '糗事'
    author = list()
    content = list()
    for url in web_url:
        print (url)
        get_data(url)
    write_excel(book,sheet_name,author,content)
