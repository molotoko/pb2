__author__ = 'lisa'
# -*- coding: utf-8 -*-

#====================================================================

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from paste.models import Paste, PasteForm
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
import re

#====================================================================

def paste_list(request):
    #object = Paste.objects.get(id=object_id)
    object_list = Paste.objects.all()
    return render_to_response('base.html', {'object_list': object_list})

#====================================================================

def paste_detail(request, object_id):
    if re.match(r'^\d+$', object_id):
        object = get_object_or_404(Paste, id=object_id)
        if object.exposure == 1:
            raise Http404("Nothing found")
    else:
        object = get_object_or_404(Paste, uu_id=object_id)
    return render_to_response('paste_detail.html', {'object': object})

#====================================================================

def create_paste(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save()
            if paste.exposure == 1:
                url = reverse('paste_detail', args=[str(paste.uu_id)])
            else:
                url = reverse('paste_detail', args=[str(paste.id)])
            return HttpResponseRedirect(url)
    else:
        form = PasteForm()
    return render(request, 'paste_form.html', {'form': form})

#====================================================================

def main(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save()
            if paste.exposure == 1:
                url = reverse('paste_detail', args=[str(paste.uu_id)])
            else:
                url = reverse('paste_detail', args=[str(paste.id)])
            return HttpResponseRedirect(url)
    else:
        form = PasteForm()
    return render(request, 'main.html', {'form': form})

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
