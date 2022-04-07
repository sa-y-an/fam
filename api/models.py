from unicodedata import name
from django.db import models

# Create your models here.

class Children(models.Model) :
    name = models.CharField(max_length=200)
    aadhar = models.CharField(max_length=10, unique=True)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Parent(models.Model) :
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    aadhar = models.CharField(max_length=10, unique=True)
    child = models.ForeignKey(Children, on_delete=models.CASCADE, blank=True , null=True)

    def __str__(self) -> str:
        return self.name
