from django.contrib import admin
from .models import *


class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'name_person', 'price', 'is_published')
    list_display_links = ('id', 'title', 'adress')
    search_fields = ('title', 'adress')


admin.site.register(Sales, SalesAdmin)
