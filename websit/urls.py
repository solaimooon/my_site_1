from .views import home_veiw,about_veiw,contact_veiw
from django.urls import path


urlpatterns = [
    path('Home/',home_veiw),
    path('about/',about_veiw),
    path('contact/',contact_veiw)

]
