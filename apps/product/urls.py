from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import(
    ProductListAPIView,
    ProductCreateAPIView,
    ProductDetailAPIView,
    CategoryCreateAPIView,
    CategoryListAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
)

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),

]
