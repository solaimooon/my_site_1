from django.contrib import admin
from .models import *


class contacts_admin(admin.ModelAdmin):
    list_display = ['name','email','created_time']
    search_fields = ['name','subject','message']
    list_filter = ['name']


admin.site.register(contacts,contacts_admin)

# Register your models here.
