from django.contrib import admin

from apps.mentors.models import Mentor
from utils.base_admin import BaseAdmin


@admin.register(Mentor)
class MentorAdmin(BaseAdmin):
    list_display = ('full_name', 'specialty', 'image')
    list_filter = ('full_name', 'specialty')
    search_fields = ('full_name', 'specialty')
    ordering = ('full_name',)

