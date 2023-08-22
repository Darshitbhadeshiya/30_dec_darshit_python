from django.shortcuts import render
from .models import book
from .serialize import userserializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def getdata(request):
    return render(request,'getdata.html')

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        stdata=book.objects.all()
        seril=userserializers(stdata,many=True)
        return Response(seril.data)
    return Response(seril.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) #search id
def getid(request,id):
    try:
        stid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response()
    
    seril=userserializers(stid)
    return Response(seril.data)

@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        stid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        seril=userserializers(stid)
        return Response(seril.data)
    if request.method=="DELETE":
        book.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def datasave(request):
    if request.method=='POST':
        seril=userserializers(data=request.data)
        if seril.is_valid():
            seril.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        stid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        seril=userserializers(stid)
        return Response(seril.data)
    
    if request.method=='PUT':
            seril=userserializers(data=request.data,instance=stid)
    if seril.is_valid():
            seril.save()
            return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    






