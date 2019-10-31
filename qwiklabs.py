import requests
from bs4 import BeautifulSoup
import html5lib


def qwikcount(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content,'html5lib')
	count = 0
	body = soup.body
	divTag = soup.find("div", {'class': 'public-profile__badges'})
	classes = []
	children = divTag.find_all("div",recursive = False)
	for child in children:
		count = count+1
	return count


url = "https://www.qwiklabs.com/public_profiles/f50eb710-cd80-4728-9f53-f1ffee77f4d3"
print("Number of Quest completed : ",qwikcount(url))



	# for tag in divTag:
	# 	print(tag)
	# 	tdTags = tag.find_all("div", {'class': 'public-profile__badge'})
	# 	count = count+1
	# print(count)