import os

from django import template
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext as _
from django.conf import settings

register = template.Library()


def attribute_has_error(errors, attribute_name):
  if attribute_name in errors: 
    return True
  return False

@register.simple_tag
def is_invalid(errors, attribute_name):
  error_keys = errors.keys()
  if attribute_has_error(error_keys, attribute_name):
    return "is-invalid"
  return ""

@register.simple_tag
def error_message(errors, attribute_name):
  error_keys = errors.keys()
  if attribute_has_error(error_keys, attribute_name):
    error_message = errors[attribute_name][0]
    error_message = _(error_message)
    return format_html('<div class="invalid-feedback">' + error_message + '</div>')
  return ""

@register.simple_tag
def forms_amount(form_list):
  return len(form_list) or 1


@register.simple_tag(takes_context=True)
def opportuniy_form_url(context):
  if 'opportunity' in context:
    return reverse('opportunity-detail', kwargs={'opportunity_id': context['opportunity'].id})
  return reverse('opportunity')