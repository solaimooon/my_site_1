from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# we can use (str=None,athour=None) as parameter in blow function
def blog_veiw(request, **kwargs):
    posts = post.objects.filter(status=1)
    if (kwargs.get("str") != None):
        posts = post.objects.filter(category__name=kwargs[str], status=True)
    elif (kwargs.get("aathour") != None):
        posts = post.objects.raw(
            "select p.* from auth_user a inner join پست p   on p.athour_id=a.id where a.username=%s",
            [kwargs["athour"]])
        # posts=post.objects.filter(athour__username=athour)
    context = {"posts_key": posts}
    return render(request, 'blog/blog-home.html', context)


def blog_detail_veiw(request, id):
    post_detail = post.objects.filter(pk=id, status=True)
    post_detail_notlist = post_detail[0]
    counter = post_detail_notlist.counted_view
    counter = counter + 1
    post_detail_notlist.counted_view = counter
    post_detail_notlist.save()
    context = {"post_detail_notlist_key": post_detail_notlist}
    return render(request, 'blog/blog-single.html', context)


# def category_view(request,str):

def search_post(request):
    posts=post.objects.filter(content__contains=request.GET.get("search")) | post.objects.filter(title__contains=request.GET.get('search'))
    context={"posts_key":posts}
    return render(request,'blog/blog-home.html',context)


def test_view(request):
    print(request.__dict__)
    print(request.method)
    request.GET.get()
    return render(request, 'test.html')
# Create your views here.
