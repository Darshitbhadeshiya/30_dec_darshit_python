from django.db import models
from datetime import datetime

# Create your models here.

class signup(models.Model):
   #created=models.DateTimeField(auto_now_add=True)
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Mobile=models.BigIntegerField()
    

