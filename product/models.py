from django.db import models
from account.models import CustomUser


class Raiting:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    ALL = (
        (one, '⭐️'),
        (two, '⭐⭐'),
        (three, '⭐⭐⭐'),
        (four, '⭐⭐⭐⭐'),
        (five, '⭐⭐⭐⭐⭐')
    )


class CategoryType:
    pass


class Category(models.Model):
    slug = models.SlugField('название категории для пути', max_length=50, primary_key=True)
    name = models.CharField('название категории', max_length=70, unique=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categoryes'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50, primary_key=True, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1770, null=True)
    price = models.CharField(max_length=4, null=True)
    raiting = models.PositiveSmallIntegerField(choices=Raiting.ALL, null=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_image', blank=True, null=True)
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image")

    def __str__(self):
        return self.post
