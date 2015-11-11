__author__ = 'lisa'
from django.template import Library

register = Library()

@register.inclusion_tag('test.html')
def render_sample(template='default.html'):
    return {'template': template}