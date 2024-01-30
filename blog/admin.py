from django.contrib import admin
from .models import *


class post_admin(admin.ModelAdmin):
    list_display = ['title','counted_view','status','created_date','updated_date']
    date_hierarchy = 'created_date'


admin.site.register(post, post_admin)
# Register your models here.
