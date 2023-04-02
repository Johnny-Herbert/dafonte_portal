import os

from django import template

from portal.templatetags.site_tags import page_param

register = template.Library()

@register.filter
def offset(objects_list, qtd):
    return objects_list[qtd:]
