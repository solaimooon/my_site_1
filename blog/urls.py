from .views import *
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('',blog_veiw,name='blog_home'),
    path('category/<str:str>/',blog_veiw,name='category'),
    path('athour/<str:athour>',blog_veiw,name='athour'),
    path('<int:id>/',blog_detail_veiw,name='blog_detail'),
    path('search_post/',search_post,name='search_post'),
    path('test/',test_view)
]