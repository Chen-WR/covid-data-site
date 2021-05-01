import json

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
		with open('data.json', 'r') as file:
			data = json.load(file)
		return data

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
		for country in tempdatacopy[0]:
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
		for state in tempdatacopy[0]:
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
		for area in tempdatacopy[0]:
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

	def main(self):
		self.setglobalData()
		self.setcountryData()
		self.setstateData()
		self.setareaData()


data = Data()
data.main()



