from django.contrib import admin

from .models import Product, Cart, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'name',
        'id'
    )
    list_filter = (
        'name',
        'id'
    )
    search_fields = (
        'name',
        'id'
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'name',
        'id'
    )
    list_filter = (
        'name',
        'id'
    )
    search_fields = (
        'name',
        'id'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'name',
        'id'
    )
    list_filter = (
        'name',
        'id'
    )
    search_fields = (
        'name',
        'id'
    )
