from django.contrib import admin
from .models import *


class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'price', 'adress', 'photo', 'name_person', 'contacts', 'is_published')
    list_display_links = ('created_at', 'price')
    search_fields = ('title', 'adress')
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Sales, SalesAdmin)
admin.site.register(Category, CategoryAdmin)
