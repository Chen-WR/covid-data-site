from django.shortcuts import render
from .models import World, Country, State, Area
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
import json
from .Data import Data

def index(request):
	data = Data()
	globaldata, countrydata, statedata, areadata = data.oneClick()
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
		name=countries['displayName'], 
		dates = countries['lastUpdated'][0:10]
		if not Country.objects.filter(name=name,date=dates).exists():
			detail = Country(
				name=countries['displayName'], 
				totalcase=countries['totalConfirmed'], 
				newcase=countries['totalConfirmedDelta'],
				totaldeath=countries['totalDeaths'],
				newdeath=countries['totalDeathsDelta'],
				date=dates,
			)
			detail.save()
	return HttpResponse('at index')

		