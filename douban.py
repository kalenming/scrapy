import requests
from bs4 import  BeautifulSoup

url = 'https://www.douban.com/accounts/login'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
#s.post(url,, headers=headers)  # POSTÕÊºÅºÍÃÜÂë£¬ÉèÖÃheaders
formData={  
    "redir":"https://www.douban.com",  
    "form_email":'915840827@qq.com',  
    "form_password":'sdef031',  
    "login":u'µÇÂ¼',
    'ck':'tG-S',
    'source':'None'
}  

#s.post(url,data=formData,headers=headers)  # POSTÕÊºÅºÍÃÜÂë£¬ÉèÖÃheaders
r = requests.post(url)  # ÒÑ¾­ÊÇµÇÂ¼×´Ì¬ÁË
soup = BeautifulSoup(r.text,'lxml')
pic = soup.select("#captcha_image")[0].get('src')
print (pic)
picture = input("ÊäÈëÑéÖ¤Âë£º")

captcha_id = soup.select('.captcha_block > input')[1]['value']
print (captcha_id)

formData['captcha-solution'] = picture
formData['captcha-id'] = captcha_id
r = requests.post(url,data = formData, headers=headers)
s = requests.get('https://www.oduban.com')
soup = BeautifulSoup(s.text,'lxml')
print (soup)