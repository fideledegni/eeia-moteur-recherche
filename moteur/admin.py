from django.contrib import admin
from .models import Search, Article

class SearchAdmin(admin.ModelAdmin):
  # fields = ['search_date', 'search_text', 'associated_articles']
  fieldsets = [
    ('Description',      {'fields': ['search_text', 'search_date']}),
    ('Clicked articles', {'fields': ['clicked_article_1', 'clicked_article_2', 'clicked_article_3']})
  ]


admin.site.register(Search, SearchAdmin)
admin.site.register(Article)
