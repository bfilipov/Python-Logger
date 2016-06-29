import requests, bs4
import xml.etree.ElementTree
import time
import re

def remove_tags(text):
	return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

while True:
	res = requests.get('http://www.thevoice.bg/news/specheli-bileti-za-skrillex#contact-form')
	res.raise_for_status()#If we made a bad request (non-200 response), we can raise it with Response.raise_for_status():
	page = bs4.BeautifulSoup(res.text,"html.parser")
	element = page.select_one('.info_canvas')
	a = remove_tags(str(element))

	a = a.split('\n') #a[1] - autjor, a[2]-name of song a[3]-time
	pattern = re.compile("\w*(SKRILLEX|Skrillex|skrillex)\w*")
	if not(pattern.match(a[1]) == None):
		print('We got a match be bace!')
		f = open('skrillex.txt','a')
		f.write(a[1]+a[2]+a[3]+'\n')
		f.close()
	   

	time.sleep(60)
	print('check again...')

