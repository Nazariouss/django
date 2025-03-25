from django.contrib import admin
from .models import Task
from .models import AppInfo

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed', 'created_at', 'due_date')
    list_filter = ('is_completed', 'due_date')
    search_fields = ('title', 'description')

admin.site.register(AppInfo)
