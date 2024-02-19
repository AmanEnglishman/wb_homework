from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import(
    ProductListAPIView,

)

urlpatterns = [

    path('', ProductListAPIView.as_view(), name='product-list')
]
