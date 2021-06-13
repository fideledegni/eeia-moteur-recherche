from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # ex: /moteur/api/get-articles/aluminium
  path('api/get-articles/<str:text>', views.search, name='search'),
  # ex: /moteur/api/save-clicks/télé/télévision,téléphone
  path('api/save-clicks/<str:text>/<str:clicks>', views.saveClicks, name='saveClicks')
]
