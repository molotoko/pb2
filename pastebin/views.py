__author__ = 'lisa'

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
    return render_to_response('paste_list.html', {'object_list': object_list})

#====================================================================

def paste_detail(request, object_id):
    object = Paste.objects.get(id=object_id)
    return render_to_response('paste_detail.html', {'object': object})

#====================================================================

@csrf_exempt
def create_paste(request):
    form = PasteForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render_to_response('paste_form.html', {'form': form})

#====================================================================

class CreatePasteView(CreateView):
    model = Paste
    template_name = 'create_paste.html'
    fields = ['title', 'poster', 'syntax', 'content', 'timestamp']

    def get_success_url(self):
        return reverse('paste_list')
