from django.contrib import admin

from .models import (MyUser, User)


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
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


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
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
