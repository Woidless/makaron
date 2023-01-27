from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serilazers import ProductSerializer, CategorySerializer
from .models import Product, Category

#
# @api_view(['GET'])
# def product(request):
#     product = Product.objects.all()
#     serializer = ProductSerializer(product, many=True)
#     return Response(serializer.data)
#
#
# class CategoryViewSet(APIView):
#     def get(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
#
#     # def post(self, request):
#     #     category = request.data.get('post')
#     #     serializer = CategorySerializer(data=category)
#     #     if serializer.is_valid(raise_exception=True):
#     #         post_saved = serializer.save()
#     #     return Response(serializer.data)
#
#
# class ProductViewSet(APIView):
#     def get(self, request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(data=product, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         post = request.data
#         serializer = ProductSerializer(data=post)
#         if serializer.is_valid(raise_exception=True):
#             product_saved = serializer.save()
#         return Response(serializer.data)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

