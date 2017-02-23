from bs4 import  BeautifulSoup
import requests
import time
import re
import json

session = requests.session()
session.cookies.set("tnet", "218.108.215.127")

index_url = "http://www.tianyancha.com/company/2316265706"
tongji_url = "http://www.tianyancha.com/tongji/2316265706.json?random=%s" % (int(time.time()) * 1000)
api_url = "http://www.tianyancha.com/company/2316265706.json"

public_headers = {
        "User-Agent": "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
        }

api_headers = public_headers.copy()
api_headers.update({
        "Tyc-From": "normal",
        "Accept": "application/json, text/plain, */*",
        "Referer": index_url,
            
    })

index_page = session.request("GET", index_url, headers = public_headers)

soup = BeautifulSoup(index_page.text,'lxml')
js_url = soup.select('script')[4].get('src')
print (js_url)

js_page = session.request("GET", js_url, headers = public_headers)
# soup = BeautifulSoup(js_page.text,'lxml')

sgattrs = json.loads(re.findall(r"n\._sgArr=(.+?);", str(js_page.content))[0])
print (sgattrs)

tongji_page = session.request("GET", tongji_url, headers = api_headers)
print (tongji_page.content)
js_code = "".join([ chr(int(code)) for code in tongji_page.json()["data"]["v"].split(",") ])
token = re.findall(r"token=(\w+);", js_code)[0]
print("token:", token)

fxck_chars = re.findall(r"\'([\d\,]+)\'", js_code)[0].split(",")
sogou = sgattrs[9] # window.$SoGou$ = window._sgArr[9]
utm = "".join([sogou[int(fxck)] for fxck in fxck_chars])    # if(window.wtf){var fxck = window.wtf().split(",");var fxckStr = "";for(var i=0;i<fxck.length;i++){fxckStr+=window.$SoGou$[fxck[i]];}document.cookie = "_utm="+fxckStr+";path=/;";window.wtf = null;}
print("utm:", utm)

session.cookies.set("token", token)
session.cookies.set("_utm", utm)

r = session.request("GET", api_url, 
        headers = api_headers)
        
print(r.json())