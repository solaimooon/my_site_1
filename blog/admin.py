from django.contrib import admin
from .models import *


class category_admin(admin.ModelAdmin):
    list_display = ['category']


class post_admin(admin.ModelAdmin):
    list_display = ['title', 'athour','counted_view', 'status', 'created_date', 'updated_date']
    date_hierarchy = 'created_date'
    list_filter = ['athour']


admin.site.register(post, post_admin)
admin.site.register(category)



# Register your models here.
