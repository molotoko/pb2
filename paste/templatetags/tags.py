__author__ = 'lisa'
from django.template import Library
from paste.models import Paste

register = Library()

#====================================================================

@register.inclusion_tag('sidebar.html')
def sidebar():
    return {'object_list': Paste.objects.exclude(exposure=1)}

#====================================================================
