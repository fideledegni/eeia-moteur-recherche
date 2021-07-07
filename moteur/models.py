from django.db import models
from datetime import timedelta
from django.utils import timezone

class Search(models.Model):
  search_text = models.CharField(max_length=200)
  search_date = models.DateTimeField('search date')
  clicked_article_1 = models.CharField(max_length=200)
  clicked_article_2 = models.CharField(max_length=200)
  clicked_article_3 = models.CharField(max_length=200)
  
  def was_searched_recently(self):
    return self.search_date >= timezone.now() - timedelta(days=1)

  def __str__(self):
    return self.search_text
   

# def default_top_search_texts():
#   return []
class Article(models.Model):
  name = models.CharField(max_length=200)
  image_name = models.CharField(max_length=50)
  description = models.CharField(max_length=500)

  def get_top_search_texts(self):
    st = Search.objects.filter(clicked_article_1=self.name)
    return list(s.search_text for s in st)

  def __str__(self):
    return self.name
