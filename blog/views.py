from django.shortcuts import render
from  .models import *
from django.http import HttpResponse


def blog_veiw(request):
    posts=post.objects.filter(status=1)
    context={"posts_key":posts}
    return render(request, 'blog/blog-home.html',context)


def blog_detail_veiw(request):
    return render(request, 'blog/blog-single.html')
# Create your views here.
