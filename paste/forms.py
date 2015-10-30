__author__ = 'lisa'

from django import forms

class AddForm(forms.Form):
    title = forms.CharField()
    syntax = forms.IntegerField()
    poster = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    #timestamp = forms.DateTimeField(widget=datetime.datetime.now)