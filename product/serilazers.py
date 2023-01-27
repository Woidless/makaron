from rest_framework import serializers
from .models import Product, Category, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = ProductImageSerializer(instance.image.all(),
                                                          many=True,
                                                          context=self.context).data
        return representation


class ProductImageSerializer(serializers.ModelSerializer):
    model = ProductImage
    fields = '_all__'


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'
