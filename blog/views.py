from django.shortcuts import render
from django.http import HttpResponse


def blog_veiw(request):
    return render(request, 'blog/blog-home.html')


def blog_detail_veiw(request):
    return render(request, 'blog/blog-single.html')
# Create your views here.
