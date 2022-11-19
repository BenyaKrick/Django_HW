from django.contrib import admin
from .models import *


class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'content', 'price', 'adress', 'photo', 'name_person', 'contacts',
                    'is_published')
    list_display_links = ('title', 'price')
    search_fields = ('title', 'adress')
    list_editable = ('is_published',)
    list_filter = ('created_at', 'category')
    sortable_by = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Sales, SalesAdmin)
admin.site.register(Category, CategoryAdmin)
