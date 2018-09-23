from bs4 import BeautifulSoup
from urllib import request

url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"

html = request.urlopen(url)

doc =BeautifulSoup(html,"html.parser")


with open('out.html','w',encoding="utf-8") as d:
	for k in doc.find_all('pre'):
		d.write(str(k)+"<br>")
d.close()
