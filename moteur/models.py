from django.db import models
from django.contrib.postgres.fields import ArrayField

class Search(models.Model):
  search_text = models.CharField(max_length=200)
  search_date = models.DateTimeField('date de recherche')
  associated_clicks = ArrayField(
      models.CharField(max_length=200, blank=True)
    )
   


class Article(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
