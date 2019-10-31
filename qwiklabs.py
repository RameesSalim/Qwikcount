import requests
from bs4 import BeautifulSoup
import html5lib
import sys

_cache = {}

def _read(url):
	text = _cache.get(url)
	if text is None:
		text = requests.get(url).text
		if not text:
			raise Exception('Empty response. Check connectivity.')
		_cache[url] = text
	return text

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

if sys.version_info[0] ==2:
	input = raw_input

input_file = input('Enter input file name: ')
# input_file = 'file.csv'
output_file = input('Enter output file name (Default output.csv): ')

if not output_file.replace(' ', ''):
	output_file = 'output.csv'

with open(input_file, 'r') as fin:
	with open(output_file, 'w') as fout:
		line0=fin.readline()
		for line in fin:
			print(line)
			print('Fetching contributions: ')
			try:
				count = str(qwikcount(line[0]))
			except Exception as e:
				print('Failedaaa: ' )
				print(e)
			fout.write(line[:-1] + ',' + count + '\n')
