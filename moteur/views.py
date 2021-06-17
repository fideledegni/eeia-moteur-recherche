from django.shortcuts import render #, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden #, HttpResponse
from django.utils import timezone
from .models import Search, Article
import json

IS_LEARNING = True # set to False when learning finished

"""
  May be usefull for handling different ways of writing the same name : télé or tele for eg.
  Anyway, we should use non accented caracters...
"""
accent = ['À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'à', 'á', 'â', 'ã', 'ä', 'å', 'Ç', 'ç', 'Ð', 'È', 'É', 'Ê', 'Ë', 'è', 'é', 'ê', 'ë', 'Ì', 'Í', 'Î', 'Ï', 'ì', 'í', 'î', 'ï', 'Ñ', 'ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø', 'ò', 'ó', 'ô', 'õ', 'ö', 'Ù', 'Ú', 'Û', 'Ü', 'ù', 'ú', 'û', 'ü', 'Ý', 'ý', 'ÿ']
traite = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'n', 'n', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'y', 'y', 'y']



# Home
def index(request):
	return render(request, 'moteur/index.html')



def save_search(text):
  s = Search(search_text=text, search_date=timezone.now())
  s.save()
  return s.id

def update_search(search_id, click_number, article_name):
  # search_by_id = get_object_or_404(Search, pk=search_id)
  s = Search.objects.get(pk=search_id)
  if click_number == 1: s.clicked_article_1 = article_name
  if click_number == 2: s.clicked_article_2 = article_name
  if click_number == 3: s.clicked_article_3 = article_name
  s.save()


def get_search_results(text, articles_list, searches_list):
  print("*****In get_search_results*****", "text: ", text)
  print("*****In get_search_results*****", "articles_list: ", articles_list)
  print("*****In get_search_results*****", "searches_list: ", searches_list)
  search_id = None
  if IS_LEARNING: search_id = save_search(text)
  res = {"list": articles_list, "search_id": search_id} if IS_LEARNING else {"list": articles_list}
  return res


# API endpoints:

# def search(request, text):
def search(_, text):
  articles = Article.objects.all().values('id', 'name', 'description')
  articles_list = list(articles) # we must convert the QuerySet to a list object
  searches = Search.objects.order_by('-search_date').values('id', 'search_text', 'search_date', 'clicked_article_1', 'clicked_article_2', 'clicked_article_3')
  # searches = Search.objects.all().values('id', 'search_text', 'search_date', 'clicked_article_1', 'clicked_article_2', 'clicked_article_3')
  searches_list = list(searches)
  res = get_search_results(text, articles_list, searches_list)
  return JsonResponse(res)


def save_click(request):
  if request.method == "POST" and IS_LEARNING:
    data = json.loads(request.body.decode('utf-8'))
    search_id = data['search_id']
    click_number = data['click_number']
    article_name = data['article_name']
    if search_id and click_number <= 3:
      try   : update_search(search_id, click_number, article_name)
      except: pass
    return JsonResponse({"OK": True})
  return HttpResponseForbidden() # GET not allowed
