from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # ex: /moteur/api/get-articles/aluminium
  path('api/get-articles/<str:text>', views.search, name='search'),
  # ex: /moteur/api/save-click (only POST requests here)
  path('api/save-click', views.save_click, name='save_clicks')
]
