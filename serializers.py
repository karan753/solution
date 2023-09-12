# serializers.py
from rest_framework import serializers
from .models import CustomUser, Content

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone', 'address', 'city', 'state', 'country', 'pincode']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'summary', 'categories', 'author']
