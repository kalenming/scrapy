import urllib
import urllib2
import cookielib

raw_cookies = 'll="108288"; bid=UvBVmje89BA; ps=y; _pk_id.100001.8cb4=2067783e92606a99.1481614287.2.1481618759.1481614441.; __utma=30149280.633159264.1481614304.1481614304.1481618523.2; __utmz=30149280.1481614304.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=30149280; ue="915840827@qq.com"; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utmb=30149280.7.10.1481618523; __utmv=30149280.6972; _vwo_uuid_v2=F6DFCC3878FF84499F50ECED6B710D23|3753cf31ebf9099c5d5375aebd9cb508; ap=1; dbcl2="69727163:h9WuEsxPbN4"; ck=dKua'
'''cookies = {}
for line in raw_cookies.split(';'):
  key,value = line.split('=',1)
  cookies[key] = value'''
login_url = 'https://www.douban.com/accounts/login'
post_url = 'https://www.douban.com'

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
h = urllib2.urlopen(login_url)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'

values = {'username':'915840827@qq.com',
          'password':'sdef031'}
headers = {'User_agent':user_agent,'Referer':'http://www.jb51.net/article/69138.htm'}
data = urllib.urlencode(values)
req = urllib2.Request(post_url,data = data,headers = headers)
print req
res = urllib2.urlopen(req)
text = res.read()
print text