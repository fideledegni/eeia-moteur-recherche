from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # ex: /moteur/api/get-articles?search=aluminium
  path('api/get-articles', views.search, name='search'),
  # ex: /moteur/api/save-click (only POST requests here)
  path('api/save-click', views.save_click, name='save_clicks')
]
