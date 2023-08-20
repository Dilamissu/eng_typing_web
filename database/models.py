from typing import Any
from django.db import models

"""
migrate database:
python manage.py makemigrations database
python manage.py migrate database
python manage.py runserver 0.0.0.0:8000

open powershell:
python manage.py shell

add object:
from .models import <object-class>
<object-class>.objects.create(<params>)

exit the shell:
exit()
"""

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=False,default='Title unknown')
    article = models.TextField(null=False)
    length = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if not self.length:
            self.length = len(str(self.article))
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title, self.article