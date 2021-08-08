# from django.shortcuts import render #, get_object_or_404
from django.utils import timezone
from unidecode import unidecode # used to remove accent
from .models import Search, Article
from random import shuffle

IS_LEARNING = True # set to False when learning finished
from eeia_moteur_recherche.settings import DEBUG


def debug(func):
  """Quick decorator for debugging purpose."""
  def wrapper(*args, **kwargs):
    args_print   = ";\n\n".join(str(arg) for arg in args)
    kwargs_print = ";\n\n".join(f"{key}={value}" for key, value in kwargs.items())
    print(f"\n*****DEBUG: {func.__name__} called with args:\n{args_print}\n"
          f"and with kwargs:\n{kwargs_print}*****\n")
    return func(*args, **kwargs)
  return wrapper if DEBUG else func


def remove_accent(string):
  """ Clean up specials characters in a 'string'.

  Args:
    string (str): string to clean up

  Returns:
    str: string cleaned
  """
  string = string.lower()
  return unidecode(string)


def save_search(text):
  """Save the text the user searched in the database

  Args:
    text (str): text searched

  Returns:
    (int | None): the id of the search in the database or None
  """
  # SAVE search text ONLY IF non-empty string
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


def add_search_id(collection: dict, search_id: int):
  """Add the search id to a collection"""
  if search_id:
    collection["search_id"] = search_id


def default_model(text, articles_list, searches_list):
  # The filter to be optimized !
  def ranker(article):
    return text in remove_accent(article['name'])
  # Shuffle to avoid having the same order
  # for same-scored articles
  shuffle(articles_list)
  return sorted(articles_list, key=ranker, reverse=True)


# @debug
def get_search_results(text, articles_list, searches_list, model=default_model):
  """Utils for the search engine. Fetch all the articles that match the searched text
  using the given model

  Args:
    text (str): searched text
    articles_list (list): arrray containing the articles in the database
    searches_list (list): array containing all the searches already done
    model (func, optional): model to apply to get the score of each articles.
      Defaults to 'default_model'.

  Returns:
    dict: the result is on the format {"list": array_of_result}
  """
  text = remove_accent(text)
  search_id = None
  res = { "list": model(text, articles_list, searches_list) }
  if IS_LEARNING:
    search_id = save_search(text)
  add_search_id(res, search_id)
  return res


def fetch_all(transformer=lambda x: x):
  """ Fetch all the data in our database

  Args:
    transformer (func, optional): A function to apply to the data fetched.
      Defaults to lambda x: x (identity).

  Returns:
    tuple: articles, searches of the database
  """
  articles = transformer(Article.objects.all().values())
  searches = transformer(Search.objects.order_by('-search_date').values())
  return articles, searches



# ----------------------------+
# MODEL 2 using edit distance |
# ----------------------------+
from .utils import levenshtein, generate_tokens

DIST_MIN = 2


def get_score(source, target, distance=levenshtein):
  """Compute a score using the given edit distance in args.

  Args:
    source (str): searched text
    target (str): data in which we are searching
    distance (func, optional): Edit distance to use. 
      Defaults to 'levenshtein'. But we can use 
      'damerau_levenshtein'

  Returns:
    int: score 
  """
  # clean up special characters
  source = remove_accent(source)
  target = remove_accent(target)

  # generate tokens
  tokens = generate_tokens(target)
  mindist = float('inf')
  for token in tokens:
    # take into account the default model
    # if the character is in the target, then
    # return the minimal score
    if source in token:
      return 0
    mindist = min(mindist, distance(source, token))
  return mindist


def close_enough(source, target):
  return get_score(source, target) < DIST_MIN