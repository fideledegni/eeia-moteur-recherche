from django.shortcuts import render #, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden #, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .controllers import fetch_all, get_search_results, update_search, IS_LEARNING


# HOME
def index(request):
	return render(request, 'moteur/index.html')


# GET ARTICLES
def search(request):
  text = request.GET.get('search', '')
  articles_list, searches_list = fetch_all(transformer=list) # we must convert the QuerySets to list objects
  response = get_search_results(text, articles_list, searches_list)
  return JsonResponse(response, safe=False)


# SAVE ARTICLE CLICK
@csrf_exempt # This decorator marks the 'save_click' view as being exempt from the protection ensured by the middleware.
             # WE CAN CHANGE THIS BEHAVIOR AFTER !! I'M USING IT FOR SIMPLICITY SINCE THE VIEW DOESN'T WORK WITHOUT IT !
def save_click(request):
  if request.method == "POST" and IS_LEARNING:
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    search_id = data['search_id']
    click_number = data['click_number']
    article_name = data['article_name']
    if search_id and click_number <= 3:
      try   : update_search(search_id, click_number, article_name)
      except: pass
    return JsonResponse({ "OK": True })
  return HttpResponseForbidden() # GET method not allowed
