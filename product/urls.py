from django.urls import path
from . import views


urlpatterns = [
    # path('product/', views.product),
    path('category/', views.CategoryViewSet.as_view())
]