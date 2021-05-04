from django.shortcuts import render
from .models import Data, Location
# from .forms import LocationForm
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .updateDB import update
import threading
import json

def index(request):
	thread = threading.Thread(target=update)
	thread.daemon = True
	thread.start()
	return render(request, "index.html")

def locationSelection(request):
	form = LocationForm()
	return render(request, 'location.html', {'form': form })

def displayGraph(request):
	pass

