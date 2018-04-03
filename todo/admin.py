from django.contrib import admin
from todo.models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pub_date', 'done')
