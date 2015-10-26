from django.db import models
from django.core.urlresolvers import reverse
import datetime

class Paste(models.Model):
    SYNTAX_CHOICES = (
        (0, "Plain"),
        (1, "Python"),
        (2, "HTML"),
        (3, "SQL"),
        (4, "Javascript"),
        (5, "CSS"),
    )

    content = models.TextField()
    title = models.CharField(blank=True, max_length=30)
    syntax = models.IntegerField(choices=SYNTAX_CHOICES, default = 0)
    poster = models.CharField(blank=True, max_length=30)
    timestamp = models.DateTimeField(default=datetime.datetime.now, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        return '"%s" (%s) by %s' % (self.title, self.SYNTAX_CHOICES[self.syntax][1], self.poster)
            #("%s (%s)" % (self.title or "#%s" % self.id), self.get_syntax_display())

    def get_absolute_url(self):
        return reverse('paste_detail', args=[str(self.id)])

