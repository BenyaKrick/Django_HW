from django.contrib import admin
from .models import *


class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'name_person', 'price', 'adress', 'contacts', 'is_published')
    list_display_links = ('created_at', 'price')
    search_fields = ('title', 'adress')


class Category(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Sales, SalesAdmin)
