from django.db import models
from datetime import datetime


# Create your models here.

class user(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)


class contact(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    massage=models.TextField()


