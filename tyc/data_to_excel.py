#将mongodb的数据写入excel
from pymongo import MongoClient
import xlwt

client = MongoClient('localhost', 27017)
tyc = client.tyc
collection = tyc.company_person
enterprises = collection.find()
alls = list()
for enterprise in enterprises:
    datas = enterprise['data']
    datas = datas[4:]
    for data in datas:
        print (data)
        company = {
        'name' : data['name'],
        'legalPersonName' : data['legalPersonName'],
        'industry' : data['industry'],
        'regStatus' : data['regStatus'],
        'base' : data['base'],
        'regCapital':data['regCapital']
        }
        alls.append(company)

book = xlwt.Workbook()
sheet = book.add_sheet('enterprise')
sheet.write(0,0,'企业名称')
sheet.write(0,1,'法人')
sheet.write(0,2,'所在省市')
sheet.write(0,3,'行业')
sheet.write(0,4,'状态')
sheet.write(0,5,'注册资本')
for i in range(0,len(alls)):
    sheet.write(i+1,0,alls[i]['name'])
    sheet.write(i+1,1,alls[i]['legalPersonName'])
    sheet.write(i+1,2,alls[i]['base'])
    sheet.write(i+1,3,alls[i]['industry'])
    sheet.write(i+1,4,alls[i]['regStatus'])
    sheet.write(i+1,5,alls[i]['regCapital'])
book.save(r'C:\Users\Administrator\Desktop\enterprise.xls')



#对企业名进行处理
import pandas as pd
import os
os.chdir('C:\\Users\\Administrator\\Desktop\\')
df = pd.read_excel('enterprise.xls')
names = df['企业名称']
names = list(names)
enters = list()
for name in names:
    try:
        name = name.replace('<em>','')
        name = name.replace('</em>','')
    except Exception as e:
        print ('no em!')
    enters.append(name)
book = xlwt.Workbook()
sheet = book.add_sheet('enterprise')
sheet.write(0,0,'企业名称')
for i in range(0,len(enters)):
    sheet.write(i+1,0,enters[i])

book.save(r'C:\Users\Administrator\Desktop\enterprise1.xls')