from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'completed')
    list_editable = ('completed',)
    search_fields = ('description',)
