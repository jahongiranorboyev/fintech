from django.contrib import admin

from utils.base_admin import BaseAdmin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(BaseAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',)
