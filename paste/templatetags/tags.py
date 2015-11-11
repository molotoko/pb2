__author__ = 'lisa'
from django.template import Library
from paste.models import Paste

register = Library()

@register.inclusion_tag('test.html')
def render_sample(template='default.html'):
    return {'template': template}

#====================================================================

@register.inclusion_tag('sidebar.html')
def sidebar():
    return {'object_list': Paste.objects.all()}
