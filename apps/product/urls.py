from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import(
    ProductListAPIView,
    ProductCreateAPIView,
    ProductDetailAPIView,
)

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),

]
