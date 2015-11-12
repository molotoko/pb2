# -*- coding: utf-8 -*-
#===========================================================

from django.db import models
from django import forms
from django.core.urlresolvers import reverse
import datetime
import uuid

#===========================================================

class Paste(models.Model):
    SYNTAX_CHOICES = (
        (0, "Plain"),
        (1, "Python"),
        (2, "HTML"),
        (3, "SQL"),
        (4, "Javascript"),
        (5, "CSS"),
    )
    EXPIRATION_CHOICES = (
        (0, "Never"),
        (1, "10 Minutes"),
        (2, "1 Hour"),
        (3, "1 Day"),
        (4, "1 Week"),
        (5, "2 Weeks"),
        (6, "1 Month"),
    )

    content = models.TextField()
    title = models.CharField(blank=True, max_length=30)
    syntax = models.IntegerField(choices=SYNTAX_CHOICES, default = 0)
    poster = models.CharField(blank=True, max_length=30)
    expiration = models.IntegerField(choices=EXPIRATION_CHOICES, default = 0)
    timestamp = models.DateTimeField(default=datetime.datetime.now, blank=True)
    #uu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        return '[%s] "%s"' % (self.SYNTAX_CHOICES[self.syntax][1], self.title)

    def get_absolute_url(self):
        return reverse('paste_detail', args=[str(self.id)])

#===========================================================

# Создание формы из модели Paste
class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ['content', 'title', 'poster', 'syntax', 'expiration']
        exclude = ['timestamp']
        widgets = {
          'content': forms.Textarea(attrs={'rows':15, 'cols':100}),
        }
