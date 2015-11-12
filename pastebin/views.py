__author__ = 'lisa'
# -*- coding: utf-8 -*-

#====================================================================

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from paste.models import Paste, PasteForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

#====================================================================

def paste_list(request):
    #object = Paste.objects.get(id=object_id)
    object_list = Paste.objects.all()
    return render_to_response('base.html', {'object_list': object_list})

#====================================================================

def paste_detail(request, object_id):
    object = Paste.objects.get(id=object_id)
    return render_to_response('paste_detail.html', {'object': object})

#====================================================================

@csrf_exempt
def create_paste(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PasteForm()

    return render_to_response('paste_form.html', {'form': form})

#====================================================================

class CreatePasteView(CreateView):
    model = Paste
    template_name = 'create_paste.html'
    fields = ['title', 'poster', 'syntax', 'content', 'timestamp']

    def get_success_url(self):
        return reverse('paste_list')

#====================================================================

@csrf_exempt
def main(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PasteForm()
    return render_to_response('main.html', {'form': form})

#====================================================================

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Insert something.')
        elif len(q) > 20:
            errors.append('Insert something up to 20 symbols.')
        else:
            pasts = Paste.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'pasts': pasts, 'query': q})

    return render_to_response('base.html', {'errors': errors})
