import json
from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def strtolist(context, data):
    dt = json.loads(data)
    return dt
