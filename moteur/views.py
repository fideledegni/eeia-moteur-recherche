from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Search, Article

def index(request):
	return render(request, 'moteur/index.html')


# API endpoints:

def search(request, text):
  # latest_search_list = Search.objects.order_by('-search_date')[:5]
  # searches = get_object_or_404(Search)
  response = "You're looking at the results of text '%s'."
  return HttpResponse(response % text)


def saveClicks(request, text, clicks):
  # save clicks for searched text
  response = "Clicks saved for text '{}' and clicks '{}'.".format(text, clicks)
  return HttpResponse(response)

