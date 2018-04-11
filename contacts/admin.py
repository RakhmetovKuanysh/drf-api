from django.contrib import admin
from contacts.models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'phone_num', 'description', 'pub_date')
