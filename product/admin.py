from django.contrib import admin
from .models import Product, Category, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 5
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


# class ProductImageInlines(admin.TabularInline):
#     model = Product
#     max_num = 3
#     min_num = 1
#
#
# @admin.register(Product)
# class ProductAdmins(admin.ModelAdmin):
#     inlines = [ProductImageInlines]


admin.site.register(Category)
