from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("task_id", "text", "time", "status")
    readonly_fields = ("task_id", "text", "time", "status")
    list_filter = ('status', 'time')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


