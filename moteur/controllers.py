# from django.shortcuts import render #, get_object_or_404
from django.utils import timezone
from unidecode import unidecode # used to remove accent
from .models import Search, Article

IS_LEARNING = True # set to False when learning finished
from eeia_moteur_recherche.settings import DEBUG


def debug(func):
  def wrapper(*args, **kwargs):
    args_print   = ";\n\n".join(str(arg) for arg in args)
    kwargs_print = ";\n\n".join(f"{key}={value}" for key, value in kwargs.items())
    print(f"\n*****DEBUG: {func.__name__} called with args:\n{args_print}\n"
          f"and with kwargs:\n{kwargs_print}*****\n")
    return func(*args, **kwargs)
  return wrapper if DEBUG else func


def remove_accent(string):
  string = string.lower()
  return unidecode(string)


def save_search(text):
  # SAVE search text ONLY IF non-empty string? YES!!
  if text:
    s = Search(search_text=text, search_date=timezone.now())
    s.save()
    return s.id
  return

def update_search(search_id, click_number, article_name):
  # search_by_id = get_object_or_404(Search, pk=search_id)
  s = Search.objects.get(pk=search_id)
  if   click_number == 1: s.clicked_article_1 = article_name
  elif click_number == 2: s.clicked_article_2 = article_name
  elif click_number == 3: s.clicked_article_3 = article_name
  s.save()


def add_search_id(collection, search_id):
  if search_id:
    collection["search_id"] = search_id


def default_model(text, articles_list, searches_list):
  # The filter to be optimized!
  def filter_func(article):
    return text in remove_accent(article['name'])
  filtered_articles = filter(filter_func, articles_list)
  return list(filtered_articles)



@debug
def get_search_results(text, articles_list, searches_list, model=default_model):
  text = remove_accent(text)
  search_id = None
  res = { "list": model(text, articles_list, searches_list) }
  if IS_LEARNING:
    search_id = save_search(text)
  add_search_id(res, search_id)
  return res


def fetch_all(transformer=lambda x: x):
  articles = transformer(Article.objects.all().values())
  searches = transformer(Search.objects.order_by('-search_date').values())
  return articles, searches
