from django.contrib import admin
from .models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']
