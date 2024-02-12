from django import template
from blog.models import *
register = template.Library()


@register.simple_tag
def simpel_template_tag ():
    return "heksdg;sdgodsijkhjkhjkhjkhjkhjkjhkggkhlkjdroijgodijyoidjgiportoojktpohjd"


@register.filter
def contatnt_fileter(content,number):
    return content[:20:]


@register.inclusion_tag('blog/popular_post.html')
def popular_post():
    posts=post.objects.all().order_by('published_date')[0:1]
    return {'posts':posts}


@register.inclusion_tag('blog/category.html')
def category_post():
    all_cetegory=category.objects.all()
    #print(all_cetegory)
    dict_rasposnse = {}
    for cat in all_cetegory:
        posts=post.objects.all()
        posts_filtering=posts.filter(category=cat).count()
        print(posts_filtering)
        dict_rasposnse.update({cat:posts_filtering})
        print(dict_rasposnse)

    return {'result':dict_rasposnse}



