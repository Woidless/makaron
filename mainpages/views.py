from django.shortcuts import render
from product.models import Product, ProductImage


def product(request):
    post = Product.objects.all()
    post_image = ProductImage.objects.all()
    context = {
        'post': post,
        'post_image': post_image
    }

    return render(request, 'main/index.html', context=context)