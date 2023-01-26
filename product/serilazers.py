from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'
