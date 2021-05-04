from .models import Data, Location
from .data.Data import Datas

def update():
	data = Datas()
	globaldata, countrydata, statedata, areadata = data.oneClick()
	# if not World.objects.filter(date=globaldata[0]['lastUpdated'][0:10]).exists() and not Country.objects.filter(date=countrydata[0]['lastUpdated'][0:10]).exists() and not State.objects.filter(date=statedata[0]['lastUpdated'][0:10]).exists() and not Area.objects.filter(date=areadata[0]['lastUpdated'][0:10]).exists():
	for world in globaldata:
		dates = world['lastUpdated'][0:10]
		if not Data.objects.filter(date=dates).exists():
			dataobj = Data(
				name_id=world['id'],
				totalcase=world['totalConfirmed'], 
				newcase=world['totalConfirmedDelta'],
				totaldeath=world['totalDeaths'],
				newdeath=world['totalDeathsDelta'],
				date=dates,
			)
			dataobj.save()
			worldobj = Location(
				name=world['displayName'], 
				name_id=world['id'],
				location_type="world",
				data=dataobj,
			)
			worldobj.save()

	for countries in countrydata:
		name_id = countries['id'] 
		dates = countries['lastUpdated'][0:10]
		if not Data.objects.filter(name_id=name_id).filter(date=dates).exists():
			dataobj = Data(
				name_id=countries['id'],
				totalcase=countries['totalConfirmed'], 
				newcase=countries['totalConfirmedDelta'],
				totaldeath=countries['totalDeaths'],
				newdeath=countries['totalDeathsDelta'],
				date=dates,
			)
			dataobj.save()
			countryobj = Location(
				name=countries['displayName'],
				name_id=countries['id'],
				parent_id=countries['parentId'],
				location_type="country", 
				data=dataobj,
			)
			countryobj.save()

	for states in statedata:
		name_id = states['id'] 
		dates = states['lastUpdated'][0:10]
		if not Data.objects.filter(name_id=name_id).filter(date=dates).exists():
			dataobj = Data(
				name_id=states['id'],
				totalcase=states['totalConfirmed'], 
				newcase=states['totalConfirmedDelta'],
				totaldeath=states['totalDeaths'],
				newdeath=states['totalDeathsDelta'],
				date=dates,
			)
			dataobj.save()
			stateobj = Location(
				name=states['displayName'],
				name_id=states['id'],
				parent_id=states['parentId'],
				location_type="state", 
				data=dataobj,
			)
			stateobj.save()

	for areas in areadata:
		name_id = areas['id'] 
		dates = areas['lastUpdated'][0:10]
		if not Data.objects.filter(name_id=name_id).filter(date=dates).exists():
			dataobj = Data(
				name_id=areas['id'],
				totalcase=areas['totalConfirmed'], 
				newcase=areas['totalConfirmedDelta'],
				totaldeath=areas['totalDeaths'],
				newdeath=areas['totalDeathsDelta'],
				date=dates,
			)
			dataobj.save()
			areaobj = Location(
				name=areas['displayName'], 
				name_id=areas['id'],
				parent_id=areas['parentId'],
				location_type="area",
				data=dataobj,
			)
			areaobj.save()