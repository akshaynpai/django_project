from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['email','password']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblShop
        fields = "__all__"
        

class ShopVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblShopVisit
        fields = "__all__"