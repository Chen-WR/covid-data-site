from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Data, Location
# from .forms import QueryModelForm
from .updateDB import update
import threading
import json

def index(request):
	thread = threading.Thread(target=update)
	thread.daemon = True
	thread.start()
	return render(request, "index.html")

def location(request):
	return render(request, "location.html", {})

def getWorld(request):
	query = list(Location.objects.filter(location_type='world').values())
	return JsonResponse({'data':query})

def getCountry(request, *args, **kwargs):
	selectGlobal = kwargs.get('world')
	countries = list(Location.objects.filter(parent_id=selectGlobal).values())
	return JsonResponse({'data':countries})

def getState(request, *args, **kwargs):
	selectCountry = kwargs.get('country')
	states = list(Location.objects.filter(parent_id=selectCountry).values())
	return JsonResponse({'data':states})

def getArea(request, *args, **kwargs):
	selectState = kwargs.get('state')
	areas = list(Location.objects.filter(parent_id=selectState).values())
	return JsonResponse({'data':areas})

def showGraph(request):
	if request.is_ajax():
		# world = request.POST.get('world')
		# country = request.POST.get('country')
		# state = request.POST.get('state')
		# area = request.POST.get('area')
		globalID = request.POST.get('globalID')
		countryID = request.POST.get('countryID')
		stateID = request.POST.get('stateID')
		areaID = request.POST.get('areaID')
		if globalID and countryID=="0" and stateID=="0" and areaID=="0":
			dataset = Data.objects.filter(name_id=globalID)
		elif globalID and countryID and stateID=="0" and areaID=="0":
			dataset = Data.objects.filter(name_id=countryID)
		elif globalID and countryID and stateID and areaID=="0":
			dataset = Data.objects.filter(name_id=stateID)
		elif globalID and countryID and stateID and areaID:
			dataset = Data.objects.filter(name_id=areaID)
		else:
			messages.error(request, "Please select location")

	return redirect('/location/')