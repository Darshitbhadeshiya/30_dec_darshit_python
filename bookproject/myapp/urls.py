from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.getdata),
    path('getall/',views.getall),
    path('getid/<int:id>',views.getid),
    path('deleteid/<int:id>',views.deleteid),
    path('datasave/',views.datasave),
    path('updatedata/<int:id>',views.updatedata),


]