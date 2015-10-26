__author__ = 'lisa'

from django.shortcuts import render_to_response
from paste.models import Paste

def paste_list(request):
    #object = Paste.objects.get(id=object_id)
    object_list = Paste.objects.all()
    return render_to_response('paste_list.html', {'object_list': object_list})

def paste_detail(request, object_id):
    object = Paste.objects.get(id=object_id)
    return render_to_response('paste_detail.html', {'object': object})

def create_paste(request):
    #new_object = Paste.objects.create()
    return render_to_response('paste_form.html')