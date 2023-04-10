from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Products

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','name','slug','precontent','content','status','image','image2','image3']