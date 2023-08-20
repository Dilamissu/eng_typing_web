"""
URL configuration for eng_typing_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

StartApp:

python manage.py startapp <app_name>

Activate and Run:

conda activate eng_typing_django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

Create super user:
python manage.py createsuperuser

"""
from django.contrib import admin
from django.urls import path
from typing_page.views import typing_page, articles_list, article_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("eng_typing/", typing_page),
    path("", articles_list),
    path("articles/", articles_list,name='articles'),
    path("articles/detail/<int:id>", article_detail,name='article_detail')
]
