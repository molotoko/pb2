# -*- coding: utf-8 -*-

#====================================================================

from django.shortcuts import render_to_response
from paste.models import Paste

#====================================================================

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос.')
        elif len(q) > 20:
            errors.append('Введите не более 20 символов.')
        else:
            pasts = Paste.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'pasts': pasts, 'query': q})

    return render_to_response('search_form.html', {'errors': errors})

