from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def blog_veiw(request):
    posts = post.objects.filter(status=1)
    context={"posts_key":posts}
    return render(request, 'blog/blog-home.html',context)


def blog_detail_veiw(request, id):
    post_detail=post.objects.filter(pk=id, status=True)
    post_detail_notlist=post_detail[0]
    counter =post_detail_notlist.counted_view
    counter=counter+1
    post_detail_notlist.counted_view=counter
    post_detail_notlist.save()
    context={"post_detail_notlist_key":post_detail_notlist}
    return render(request, 'blog/blog-single.html',context)
# Create your views here.
