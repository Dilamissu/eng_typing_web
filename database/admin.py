from django.contrib import admin
from django.apps import apps
from database.models import Article

"""
If you want to clean the whole database, you can use:
python manage.py flush

If you want to clean the database table of a Django app, you can use:
python manage.py migrate <app-name> zero
"""

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    model = Article

    list_display = ['id', 'title', 'length','article',]
    search_fields = ['id', 'title']
    readonly_fields = ['id']

    filter_horizontal = ()
    list_filter = ()
    ordering = ('id',)
    fieldsets = [(None, {'fields': ['id', 'title', 'length']}),
                 ('Article', {'fields': ['article']}),]
admin.site.register(Article, ArticleAdmin)
