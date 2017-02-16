import requests
from bs4 import BeautifulSoup
urls = ['http://v.qq.com/x/list/movie?cate=10001&subtype=100004&offset={}' .format(i) for i in range(0,300,30)]
#print (url)
for url in urls:
	s = requests.get(url)
	soup = BeautifulSoup(s.text,'lxml')
	titles = soup.select('.list_item > a')
	# print (titles)
	for title in titles:
		title = title.get('href')
		print (title)