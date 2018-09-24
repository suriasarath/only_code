from bs4 import BeautifulSoup
from urllib import request

url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
url2 = "https://matplotlib.org/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py"
html = request.urlopen(url2)

doc =BeautifulSoup(html,"html.parser")


with open('out.html','w',encoding="utf-8") as d:

	d.write('<head><link rel="stylesheet" href="math.css"></head>')
	for k in doc.find_all('pre'):
		d.write(str(k)+"<br>")
d.close()
