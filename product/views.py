from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilazers import ProductSerializer
from .models import Product


@api_view(['GET'])
def product(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(
        {
            f'message: this is list of product: {serializer.data}'
        }
    )
