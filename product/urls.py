from django.urls import path
from . import views


urlpatterns = [
    # path('product/', views.product),
    path('category-create/', views.CategoryListView.as_view()),
    path('product-create/', views.ProductView.as_view())
]