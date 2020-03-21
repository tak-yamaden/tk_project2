from django import template
from drafts.models import Category

register = template.Library()

@register.inclusion_tag('drafts/tags/category_links.html')
def render_category_links():
    return {
        'category_list': Category.objects.all(),
    }
