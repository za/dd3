from django.shortcuts import render
from django.http import JsonResponse
from django.db import connections
from django.db.models import Count

from visitor.models import Apache

import json

# Create your views here.

def text(request):
	apachelogs_list = Apache.objects.all()
	context_dict = {'apaches': apachelogs_list}
	return render(request, 'index.html', context_dict)

def render_javascript(request):
	lists = [
		  { "date": "2015-11-28", "visit": 10 },
		  { "date": "2015-10-09", "visit": 8 },
		  { "date": "2015-11-01", "visit": 25 },
		]
	context_dict = {'lists_as_json': lists}
	return render(request, 'lists.html', context_dict)

def render_javascript2(request):
	apaches = Apache.objects.all()
	abc = []
	for apache in apaches:
		abc.append(apache)
	data_as_json = json.dumps(data.__dict__)
	context_dict = {'data_as_json': data_as_json}
	return render(request, 'logs.html', context_dict)

