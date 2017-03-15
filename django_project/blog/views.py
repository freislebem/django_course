from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'blog/home.html')

def megasena(request):
	
	valormega = 100 + 300

	coiote = {

		'valormega' : valormega
	}	
	return render(request, 'blog/megasena.html', coiote)