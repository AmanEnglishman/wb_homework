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
    ProductViewSet,
    ProductFilterListAPIView,
    CartAPIView,
    CartUpdateAPIView,
)

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('<int:pk>/viewset', ProductViewSet.as_view(), name='product-viewset'),
    path('filter/', ProductFilterListAPIView.as_view(), name='product-filter'),
    path('cart/<int:id>', CartAPIView.as_view(), name='cart'),
    path('cart/<int:id>/update/', CartUpdateAPIView.as_view(), name='cart-update'),


]
