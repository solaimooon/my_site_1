from .views import home_veiw,about_veiw,contact_veiw
from django.urls import path

app_name='websit'
urlpatterns = [
    path('',home_veiw,name='home'),
    path('about/',about_veiw,name='about'),
    path('contact/',contact_veiw,name='contact')

]
