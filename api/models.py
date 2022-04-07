from django.db import models

# Create your models here.

class Children(models.Model) :
    name = models.CharField(max_length=200)
    age = models.IntegerField()

class Parent(models.Model) :
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    child = models.ForeignKey(Children, on_delete=models.CASCADE)
