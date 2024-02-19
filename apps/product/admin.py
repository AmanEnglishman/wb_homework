from django.contrib import admin

from .models import MyProduct, product


@admin.register(MyProduct)
class MyProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email'
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


@admin.register(MyProduct)
class MyProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email'
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
