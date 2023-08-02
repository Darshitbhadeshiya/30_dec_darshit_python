from django.shortcuts import render
from .models import userinfo
from .serializers import userserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getdata(request):
    if request.method=='GET':
        userdata=userinfo.objects.all()
        stdata=userserializers(userdata,many=True)
        return Response(stdata.data)



