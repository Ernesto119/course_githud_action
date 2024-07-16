from django.contrib import admin
from .models import Task

class Task_admin(admin.ModelAdmin):
    list_filter = ["title","date"]
    search_fields =["title"]

admin.site.register(Task,Task_admin)