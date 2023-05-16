from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.models):
    class Meta:
        model = Users
        fields = "__all__"

class ProductDetailSerializer(serializers.models):
     class Meta:
          model = ProductDetail
          fields = "__all__"