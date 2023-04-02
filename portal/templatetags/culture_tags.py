import os

from django import template

from portal.templatetags.site_tags import page_param

register = template.Library()


@register.simple_tag(takes_context=True)
def get_values(context):
	values = []
	counter = 1
	while True:
		value_title = page_param(context, "value-{}-title".format(counter))
		print('value 1{}'.format(value_title))
		if "class='parameter-not-found'" in value_title:
			break
		value_description = page_param(context, "value-{}-description".format(counter))
		values.append(dict(title=value_title, description=value_description))
		print(values)
		counter += 1
	return values
