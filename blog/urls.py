from .views import *
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('',blog_veiw,name='blog_home'),
    path('blog_detail/',blog_detail_veiw,name='blog_detail'),
]