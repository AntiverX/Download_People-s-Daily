import urllib.request
from bs4 import BeautifulSoup
import datetime
import re,os
import win32api,win32con

global year,month,day
year = datetime.datetime.now().strftime('%Y')
month = datetime.datetime.now().strftime('%m')
day = datetime.datetime.now().strftime('%d')
#下载文件
def DownloadFile(url,filename):
	urllib.request.urlretrieve(url,filename)

#获取网页
def ConnectUrl(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req)
    print("get content!")
    bsObj = BeautifulSoup(html,"lxml")
    return bsObj

#生成Url
def genUrl():
	url = "http://paper.people.com.cn/rmrb/html/"+str(year)+"-"+str(month)+"/"+str(day)+"/nbs.D110000renmrb_01.htm"
	return url

#爬虫
def getRMRB():
	print("start connecting!")
	print( genUrl() )
	target = ConnectUrl(genUrl())
	print("connnect successfully!\n")
	names = target.find("div",{"id":"pageList"}).findAll("a",{"id":"pageLink"})
	link = target.find("div",{"id":"pageList"}).findAll("a",href=re.compile("pdf"))
	os.mkdir(str(year)+str(month)+str(day))
	i = 0
	for filename in names:
		url = "http://paper.people.com.cn/rmrb/page"+link[i].attrs['href'][13:]
		DownloadFile(url,str(year)+str(month)+str(day)+"/"+filename.string+".pdf")
		i = i + 1
		print(filename.string+" :success downloaded.")
	win32api.MessageBox(0, "下载完成了哦", "哈哈", win32con.MB_OK)

getRMRB()
