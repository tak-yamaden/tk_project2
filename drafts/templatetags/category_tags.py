from django import template
from django.db.models import Count
from drafts.models import Category, Draft

register = template.Library()

# @register.inclusion_tag('drafts/tags/category_links.html')
# def render_category_links():
#     ctx = {}
#     ctx['category_list'] = Category.objects.annotate(
#         count=Count('company'))
#     return ctx
@register.inclusion_tag('drafts/tags/category_links.html')
def render_category_links():
    ctx = {}
    ctx['draft_list'] = Draft.objects.annotate(
        count=Count('category'))
    return ctx