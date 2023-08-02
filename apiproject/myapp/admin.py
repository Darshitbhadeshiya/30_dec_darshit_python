from django.contrib import admin
from .models import userinfo

# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','mobile']

admin.site.register(userinfo,useradmin)

