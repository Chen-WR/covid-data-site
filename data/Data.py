import json
import requests
from bs4 import BeautifulSoup

class Data:
	def __init__(self):
		self.data = self.getData()
		self.tempdata = []
		self.globaldata = []
		self.countrydata = []
		self.statedata = []
		self.areadata = []

	# Whole Data
	def getData(self):
		url = 'https://www.bing.com/covid'
		data = requests.get(url).text
		soup = BeautifulSoup(data, 'html.parser')
		element = str(soup.find("div", id="main").find('script'))
		element = element.strip('<script type="text/javascript">var data=')
		element = element.strip(';</script>')
		json_data = json.loads(element)
		# with open('data.json', 'w+') as output:
		# 	json.dump(json_data, output, indent=4, separators=(',', ': '))
		# with open('data.json', 'r') as file:
		# 	data = json.load(file)
		return json_data

	# Extract Global Data
	def setglobalData(self):
		tempDict = {}
		for x,y in self.data.items():
			if x == "areas" and y:
				self.tempdata.append(y)
			else:
				tempDict[x] = y
		self.globaldata.append(tempDict)
		self.writeData(self.globaldata, 'globaldata')

	def setcountryData(self):
		tempdatacopy = self.tempdata.copy()
		self.tempdata = []
		for countrys in tempdatacopy:
			for country in countrys:
				tempDict = {}
				for x,y in country.items():
					if x == 'areas' and y:
						self.tempdata.append(y)
					else:
						tempDict[x] = y 
				self.countrydata.append(tempDict)
		self.writeData(self.countrydata, 'countrydata')

	def setstateData(self):
		tempdatacopy = self.tempdata.copy()
		self.tempdata = []
		for states in tempdatacopy:
			for state in states:
				tempDict = {}
				for x,y in state.items():
					if x == 'areas' and y:
						self.tempdata.append(y)
					else:
						tempDict[x] = y 
				self.statedata.append(tempDict)
		self.writeData(self.statedata, 'statedata')

	def setareaData(self):
		tempdatacopy = self.tempdata.copy()
		self.tempdata = []
		for areas in tempdatacopy:
			for area in areas:
				tempDict = {}
				for x,y in area.items():
					if x == 'areas' and y:
						self.tempdata.append(y)
					else:
						tempDict[x] = y 
				self.areadata.append(tempDict)
		self.writeData(self.areadata, 'areadata')

	def getglobalData(self):
		return self.globaldata

	def getcountryData(self):
		return self.countrydata

	def getstateData(self):
		return self.statedata

	def getareaData(self):
		return self.areadata

	def writeData(self, data, filename):
		ext = '.json'
		filename += ext
		with open(filename, 'w+') as output:
			json.dump(data, output, indent=4, separators=(',', ': '))

	def start(self):
		self.setglobalData()
		self.setcountryData()
		self.setstateData()
		self.setareaData()

def main():
	data = Data()
	data.start()

if __name__ == '__main__':
	main()

