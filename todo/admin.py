from django.contrib import admin
from .models import Task
#from django.utils import timezone

#class TaskInline(admin.TabularInline):
class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Task Details',{'fields': ['todo_text']}),
        ('Date information', {'fields': ['add_date']}),
    ]
    list_display = ('todo_text', 'add_date')
    ordering = ['add_date']
    list_filter = ['add_date']
    search_fields = ['todo_text']

admin.site.register(Task,TaskAdmin)
