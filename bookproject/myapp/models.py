from django.db import models

# Create your models here.
#createsuperuser username=book password=book@model

class book(models.Model):
    Bookname=models.CharField(max_length=30)
    Tital=models.TextField()
    Author=models.CharField(max_length=30)
    Isbn=models.BigIntegerField()
    Publisher=models.CharField(max_length=30)