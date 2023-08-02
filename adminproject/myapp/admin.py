from django.contrib import admin
from .models import product_categary,product_master

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display=['product','price','image','model','ram']

admin.site.register(product_master)
admin.site.register(product_categary,productAdmin)
