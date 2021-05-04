from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from .models import Data, Location
# from .forms import QueryModelForm
from .updateDB import update
import threading
import json

def index(request):
	# thread = threading.Thread(target=update)
	# thread.daemon = True
	# thread.start()
	return render(request, "index.html")

def location(request):
	query = Location.objects.filter(location_type='world').all()
	return render(request, "location.html", {'query':query})

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