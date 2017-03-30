# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
import xlrd
import pymongo
from flask import render_template
conn = pymongo.Connection('localhost',27017)
db = conn.Spider
account = db.jianshu


@app.route('/',methods=['GET', 'POST'])
def fans_list():
    item = list()
    for user in db.jianshu.find():
        print (user['name'])
        item.append(user)
    return render_template('index.html',data =item)

@app.route('/test',methods=['GET', 'POST'])
def test():
    file = xlrd.open_workbook('fan.xlsx')
    sheet = file.sheet_by_index(0)
    item = sheet.col_values(0)
    return render_template('test.html',data =item)

if __name__ == '__main__':
    app.run(debug=True)