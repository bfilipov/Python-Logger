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
	currSong = remove_tags(str(element)).split('\n') #currSong[1] - autjor, currSong[2]-name of song currSong[3]-time

	pattern = re.compile("\w*(SKRILLEX|Skrillex|skrillex)\w*")
	if not(pattern.match(currSong[1]) == None):
		print('We got a match!')
		f = open('skrillex.txt','a')
		f.write("{} - {}, Played at: {} \n".format(currSong[1],currSong[2],currSong[3]))
		f.close()
	   

	time.sleep(60)
	print('check again...')
