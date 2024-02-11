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
def include_test():
    posts=post.objects.all().order_by('published_date').values()
    return {'posts':posts}


