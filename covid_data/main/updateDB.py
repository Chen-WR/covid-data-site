from .models import World, Country, State, Area
from .data.Data import Data

def update():
	data = Data()
	globaldata, countrydata, statedata, areadata = data.oneClick()
	# if not World.objects.filter(date=globaldata[0]['lastUpdated'][0:10]).exists() and not Country.objects.filter(date=countrydata[0]['lastUpdated'][0:10]).exists() and not State.objects.filter(date=statedata[0]['lastUpdated'][0:10]).exists() and not Area.objects.filter(date=areadata[0]['lastUpdated'][0:10]).exists():
	for world in globaldata:
		dates = world['lastUpdated'][0:10]
		if not World.objects.filter(date=dates).exists():
			detail = World(
				name=world['displayName'], 
				totalcase=world['totalConfirmed'], 
				newcase=world['totalConfirmedDelta'],
				totaldeath=world['totalDeaths'],
				newdeath=world['totalDeathsDelta'],
				date=dates,
			)
			detail.save()

	for countries in countrydata:
		names = countries['displayName'] 
		dates = countries['lastUpdated'][0:10]
		if not Country.objects.filter(name=names).filter(date=dates).exists():
			detail = Country(
				name=countries['displayName'], 
				totalcase=countries['totalConfirmed'], 
				newcase=countries['totalConfirmedDelta'],
				totaldeath=countries['totalDeaths'],
				newdeath=countries['totalDeathsDelta'],
				date=dates,
			)
			detail.save()

	for states in statedata:
		names = states['displayName'] 
		dates = states['lastUpdated'][0:10]
		if not State.objects.filter(name=names).filter(date=dates).exists():
			detail = State(
				name=states['displayName'], 
				totalcase=states['totalConfirmed'], 
				newcase=states['totalConfirmedDelta'],
				totaldeath=states['totalDeaths'],
				newdeath=states['totalDeathsDelta'],
				date=dates,
			)
			detail.save()

	for areas in areadata:
		names = areas['displayName'] 
		dates = areas['lastUpdated'][0:10]
		if not Area.objects.filter(name=names).filter(date=dates).exists():
			detail = Area(
				name=areas['displayName'], 
				totalcase=areas['totalConfirmed'], 
				newcase=areas['totalConfirmedDelta'],
				totaldeath=areas['totalDeaths'],
				newdeath=areas['totalDeathsDelta'],
				date=dates,
			)
			detail.save()