# coding: UTF-8

import httplib
import urllib
import urllib2
import json
#import demjson
values = {}
#values[''] = ""
values['column'] = "fund_listed"
values['columnTitle'] = "%E5%9F%BA%E9%87%91%E5%85%AC%E5%91%8A"
values['pageNum'] = 2
values['pageSize'] = 3000
values['seDate'] = "%E8%AF%B7%E9%80%89%E6%8B%A9%E6%97%A5%E6%9C%9F"
params = urllib.urlencode(values) 
params= "stock=&searchkey=&plate=&category=&trade=&column=fund_listed&columnTitle=%E5%9F%BA%E9%87%91%E5%85%AC%E5%91%8A&pageNum=2&pageSize=30&tabName=latest&sortName=&sortType=&limit=&showTitle=&exchange=&fundtype=&seDate=%E8%AF%B7%E9%80%89%E6%8B%A9%E6%97%A5%E6%9C%9F"
#print params
headers = {
"Host": "www.cninfo.com.cn",
"Connection":" keep-alive",
"Content-Length":" 257",
"Accept":" application/json, text/javascript, */*; q=0.01",
"Origin":" http://www.cninfo.com.cn",
"X-Requested-With":" XMLHttpRequest",
"User-Agent":" Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Referer":" http://www.cninfo.com.cn/cninfo-new/disclosure/fund_listed",
"Accept-Encoding":" gzip, deflate",
"Accept-Language":" zh-CN,zh;q=0.8",
"Cookie":"COLLPCK=361493945; JSESSIONID=0E07A2BCD6B917B480DEF5ED76666906"
} 

DIR = "/cninfo-new/disclosure/fund_listed_latest"
URL = "www.cninfo.com.cn:80"

conn = httplib.HTTPConnection(URL) 
while (True):
	
	conn.request("POST", DIR, params, headers)  
	response = conn.getresponse()  
	print response.status, response.reason 
	

	if response.status==200:
		break
	if response.status==307:
		head = response.getheaders()
		print head [0][1]

		headers["Cookie"] =head[0][1]
	

data = response.read() 
print data
score = json.loads(data.decode('UTF-8'))
print "\n"
print score
conn.close()