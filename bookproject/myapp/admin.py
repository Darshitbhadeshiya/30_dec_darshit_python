from django.contrib import admin
from .models import book

# Register your models here.

class data(admin.ModelAdmin):
    list_display=['Bookname','Tital','Author','Isbn','Publisher']

admin.site.register(book,data)

