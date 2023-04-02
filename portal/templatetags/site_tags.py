import os

from django import template
from django.utils.html import format_html

from django.conf import settings
from portal.models import SiteParameter, PageParameter

from django.utils.translation import gettext_lazy as _
from django.utils.translation import ugettext_lazy

register = template.Library()


@register.simple_tag
def site_param(param_name):
    try:
        param = SiteParameter.objects.get(name=param_name)
        if param_name == 'head-title':
            return format_html(param.value.replace("\n", "<br />"))

        if param.file.name is not None:
            return param.file.url

        return format_html(param.value.replace("\n", "<br />"))
    except SiteParameter.DoesNotExist:
        if param_name == 'institutional-folder':
            return "static/pdf/dafonte-folder-institucional.pdf"
        elif param_name == 'head-title-icon':
            return "static/images/icons/virgula.png"
        return format_html(
            "<span class='parameter-not-found'>Parâmetro do Site \"{}\" "
            "não encontrado.</span>", param_name)


@register.simple_tag(takes_context=True)
def page_param(context, param_name):
    page = context["page"]
    try:
        param = page.parameters.get(name=param_name)
        return format_html(param.value.replace("\n", "<br />"))
    except PageParameter.DoesNotExist:
        return format_html(
            "<span class='parameter-not-found'>Parâmetro \"{}\" "
            "da Página \"{}\" não encontrado.</span>", param_name, page.slug)


@register.simple_tag
def flag_file(language_code):
    if language_code == "pt-br":
        return "flag-brazil.svg"
    if language_code == "en":
        return "flag-usa.svg"
    return "flag-none.svg"


@register.simple_tag
def checked(expected, value):
    expected = str(expected)
    value = str(value)
    return "checked" if expected == value else ""


@register.simple_tag
def selected(expected, value):
    expected = str(expected)
    value = str(value)
    return "selected" if expected == value else ""


@register.simple_tag
def classed(expected, value, classes):
    expected = str(expected)
    value = str(value)
    return classes if expected == value else ""


@register.simple_tag
def disabled(condition):
    return "disabled" if condition else ""


@register.simple_tag
def make_range(n1, n2=None, n3=None):
    n1 = int(n1)
    if n3 is not None:
        n2 = int(n2) + 1
        n3 = int(n3)
        return range(n1, n2, n3)
    elif n2 is not None:
        n2 = int(n2) + 1
        return range(n1, n2)
    return range(n1)


@register.simple_tag
def trans_lang(lang_code):
    for lang in settings.LANGUAGES:
        if lang[0] == lang_code:
            return format_html("{}", (lang[1]))


@register.simple_tag
def upfile(file_path):
    return os.path.join(settings.BASE_DIR, file_path.name)


@register.simple_tag(takes_context=True)
def page_background_cover(context):
    page = context['page']
    if page.background_image:
        return page.background_image.url
    else:
        return "/static/images/default-header.jpg"
