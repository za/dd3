from django.shortcuts import render

from visitor.models import Apache

# Create your views here.

def index(request):
	apachelogs_list = Apache.objects.all()
	context_dict = {'apaches': apachelogs_list}
	return render(request, 'index.html', context_dict)
