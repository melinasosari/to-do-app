from django.contrib import admin
from .models import Task 

# Register your models here.
@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'discription', 'created', 'is_done']
    list_filter = ['is_done']
    search_fields = ('title', 'created')