from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=15)
    

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    rate = models.CharField(max_length=10)     


class Book(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()
