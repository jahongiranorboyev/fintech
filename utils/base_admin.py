from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """Base admin class to avoid repeating read_only_fields."""
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
