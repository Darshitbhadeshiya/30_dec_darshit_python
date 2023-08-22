from rest_framework import serializers
from .models import book

class userserializers(serializers.ModelSerializer):
    class Meta:
        model=book
        fields="__all__"
