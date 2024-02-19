from django.contrib import admin

from .models import Product, Cart, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'email',
        'id'
    )
    list_filter = (
        'email',
        'id'
    )
    search_fields = (
        'email',
        'id'
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'email',
        'id'
    )
    list_filter = (
        'email',
        'id'
    )
    search_fields = (
        'email',
        'id'
    )


@admin.Product(Cart)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'email',
        'id'
    )
    list_filter = (
        'email',
        'id'
    )
    search_fields = (
        'email',
        'id'
    )
