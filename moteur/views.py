from django.shortcuts import render #, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
import json
import csv

from .controllers import fetch_all, get_search_results, update_search, IS_LEARNING
from eeia_moteur_recherche.settings import DEBUG


# HOME
def index(request):
	return render(request, 'moteur/index.html')


# GET ARTICLES
def search(request):
  text = request.GET.get('search', '')
  model_num = request.GET.get('model_num', '')
  if DEBUG: print("Got 'search' request with text: ", text)
  articles_list, searches_list = fetch_all(transformer=list) # we must convert the QuerySets to list objects
  response = get_search_results(text, articles_list, searches_list, model_num)
  return JsonResponse(response, safe=False)


# SAVE ARTICLE CLICK
def save_click(request):
  if request.method == "POST" and IS_LEARNING:
    data = json.loads(request.body.decode('utf-8'))
    if DEBUG: print("Got 'save click' request with data: ", data)
    search_id = data['search_id']
    click_number = data['click_number']
    article_name = data['article_name']
    if search_id and click_number <= 3:
      try   : update_search(search_id, click_number, article_name)
      except: pass
    return JsonResponse({ "OK": True })
  return HttpResponseForbidden() # GET method not allowed


# GET SEARCHES LIST IN CSV FORMAT
def get_csv_searches_list(_):
  _, searches_list = fetch_all(transformer=list)
  titles = ["id", "search_text", "search_date", "clicked_article_1", "clicked_article_2", "clicked_article_3"]
  # head = ",".join(titles)
  # lines = "\n".join(",".join(str(s[key]) for key in titles) for s in searches_list)
  # csvString = head + "\n" + lines
  # print(csvString)

  response = HttpResponse(
    content_type='text/csv',
    headers={'Content-Disposition': 'attachment; filename="liste_des_recherches.csv"'},
  )

  writer = csv.writer(response)
  writer.writerow(titles)
  for s in searches_list: writer.writerow(str(s[key]) for key in titles)
  return response


# GET ARTICLES LIST IN CSV FORMAT
def get_csv_articles_list(_):
  articles_list, _ = fetch_all(transformer=list)
  titles = ["id", "name", "description"]

  response = HttpResponse(
    content_type='text/csv',
    headers={'Content-Disposition': 'attachment; filename="liste_des_articles.csv"'},
  )

  writer = csv.writer(response)
  writer.writerow(titles)
  for a in articles_list: writer.writerow(str(a[key]) for key in titles)
  return response
