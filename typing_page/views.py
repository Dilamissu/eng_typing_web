from django.shortcuts import render
from django.http import HttpResponse
from database.models import Article

"""
python manage.py makemigrations typing_page
python manage.py migrate typing_page
python manage.py runserver 0.0.0.0:8000

"""

# Create your views here.

def typing_page(request):
    return render(request, "typing_page.html", {'article': 'I am a CSIE student. Which means my main course go around coding stuffs.'})

def articles_list(request):
    return render(request, "articles_list.html", {'articles': Article.objects.all()})

def article_detail(request, id):
    return render(request, "single_article.html", {'article': Article.objects.get(id=id)})