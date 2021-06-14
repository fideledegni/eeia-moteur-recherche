from django.shortcuts import render

def index(request):
	return render(request, 'moteur/index.html')

# TODO: api endpoint
