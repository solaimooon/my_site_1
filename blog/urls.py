from .views import *
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('',blog_veiw,name='blog_home'),
    path('<int:id>/',blog_detail_veiw,name='blog_detail'),
    path('test/',test_view)
]