from django.shortcuts import render
from django.http import HttpResponse


def home_veiw(request):
    return render(request,'index.html')


def about_veiw(request):
    return render(request,'about.html')


def contact_veiw(request):
    return render(request, 'contact.html')
