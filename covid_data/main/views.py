from django.shortcuts import render
import json
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
	return HttpResponse('at index')

def DBinit(request):
	try:
		with open('data.json', 'r') as file:
			data = json.load(file)
		