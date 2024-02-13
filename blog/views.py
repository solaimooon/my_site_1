from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def blog_veiw(request,str=None,athour=None):
    posts = post.objects.filter(status=1)
    if (str):
        posts = post.objects.filter(category__name=str, status=True)
    elif athour:
        posts=post.objects.raw("select p.* from auth_user a inner join پست p   on p.athour_id=a.id where a.username=%s",[athour])
    context = {"posts_key": posts}
    return render(request,'blog/blog-home.html',context)


def blog_detail_veiw(request, id):
    post_detail=post.objects.filter(pk=id, status=True)
    post_detail_notlist=post_detail[0]
    counter =post_detail_notlist.counted_view
    counter=counter+1
    post_detail_notlist.counted_view=counter
    post_detail_notlist.save()
    context={"post_detail_notlist_key":post_detail_notlist}
    return render(request, 'blog/blog-single.html',context)


#def category_view(request,str):



def test_view(request):
    return render(request,'test.html')
# Create your views here.
