import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import numpy as np

def grabJson():
	url = 'https://www.bing.com/covid'
	data = requests.get(url).text
	soup = BeautifulSoup(data, 'html.parser')
	element = str(soup.find("div", id="main").find('script'))
	element = element.strip('<script type="text/javascript">var data=')
	element = element.strip(';</script>')
	json_data = json.loads(element)
	return json_data

def printJson():
	json_data = grabJson()
	print(json.dumps(json_data, indent=4, sort_keys=True))

def makeJson():
	json_data = grabJson()
	with open('data.json', 'w+') as output:
		json.dump(json_data, output, indent=2, separators=(',', ': '))

# Return list contain dictionary with first key as displayName  
def getCountryData():
	# Country data wanted
	countryList = ["United States", "Japan"]
	# Data field wanted
	datafield = ['displayName', 'totalConfirmed', 'totalDeaths', 'totalDeathsDelta', 'totalConfirmedDelta']
	# Get big data file from HTML
	json_data = grabJson()
	# The first area key will be the world
	country_data = json_data['areas']
	dataList = []
	# filter countries in data
	for countries in country_data:
		if countries['displayName'] in countryList:
			data = {}
			for key, value in countries.items():
				if key in datafield:
					data[key] = value
			dataList.append(data)
	return dataList

# Use the dictionary list and rearrange data
def arrangeData():
	dataList = getCountryData()
	country = [i['displayName'] for i in dataList]
	label = list(dataList[0].keys())
	confirmed = [i['totalConfirmed'] for i in dataList]
	newcase = [i['totalConfirmedDelta'] for i in dataList]
	deaths = [i['totalDeaths'] for i in dataList]
	newdeath = [i['totalDeathsDelta'] for i in dataList] 
	array = [country, confirmed, deaths, newdeath, newcase]
	data = {}
	for i in range(len(label)):
		data[label[i]] = array[i]
	return data
	'''
	returns:
	[
		{'displayName': 'United States', 'totalConfirmed': 32375602, 'totalDeaths': 579162, 'totalDeathsDelta': 806, 'totalConfirmedDelta': 55477}
		{'displayName': 'India', 'totalConfirmed': 18342110, 'totalDeaths': 204444, 'totalDeathsDelta': 3279, 'totalConfirmedDelta': 353473}
		{'displayName': 'Japan', 'totalConfirmed': 575563, 'totalDeaths': 10055, 'totalDeathsDelta': 51, 'totalConfirmedDelta': 4523}
	]
	'''

# Make graph with matplotlib
def makeGraph():
	data = arrangeData()
	# data = {
	# 	'displayName': ['United States', 'Japan'], 
	# 	'totalConfirmed': [45,35], 
	# 	'totalDeaths': [38,20], 
	# 	'totalDeathsDelta': [76, 10], 
	# 	'totalConfirmedDelta': [43, 20]
	# 	}
	country = data['displayName']
	fig, ax = plt.subplots()
	# Config
	x = np.arange(len(country)) 
	width = 0.35
	ax.set_ylim([0, max(data['totalConfirmed'])+10000000])
	ax.ticklabel_format(style='plain')
	ax.set_ylabel('Population')
	ax.set_title('Covid Data')
	ax.set_xticks(x)
	ax.set_xticklabels(country)
	# Create bar for each data
	rects1 = ax.bar(x, data['totalConfirmed'], width/4, label='Total Confirmed')
	# rects2 = ax.bar(x - width/2, data['totalConfirmedDelta'], width/4, label='New Cases')
	# rects3 = ax.bar(x + width/2, data['totalDeaths'], width/4, label='Total Death')
	# rects4 = ax.bar(x + width, data['totalDeathsDelta'], width/4, label='New Death')
	# Set label above the bar
	ax.bar_label(rects1, padding=3)
	# ax.bar_label(rects2, padding=3)
	# ax.bar_label(rects3, padding=3)
	# ax.bar_label(rects4, padding=3)

	fig.tight_layout()

	plt.show()
	# for i in dir(ax):
	# 	print(i)


def main():
	makeJson()

if __name__ == '__main__':
	main()