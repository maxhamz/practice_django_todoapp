from django.contrib import admin
from .models import Task


# we create this class to enable centralized admin function for tasks
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at')


# Register your models here.
admin.site.register(Task, TaskAdmin)
