# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True)