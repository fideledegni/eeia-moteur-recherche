from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import timedelta
from django.utils import timezone

# TODO: finish models architecture!
class Search(models.Model):
  search_text = models.CharField(max_length=200)
  search_date = models.DateTimeField('date de recherche')
  associated_clicks = ArrayField(
      models.CharField(max_length=200, blank=True)
    )
  
  def was_searched_recently(self):
    return self.search_date >= timezone.now() - timedelta(days=1)

  def __str__(self):
    return self.search_text
   


class Article(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  def __str__(self):
    return self.name
