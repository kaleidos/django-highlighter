from django.db import models
from .settings import *

HIGHLIGHT_PRIORITY_CHOICES = [ (x,x) for x in range(*HIGHLIGHTER_PRIORITY_RANGE) ]

class HighlightedManager(models.Manager):
    def get_query_set(self):
        return super(HighlightedManager, self).get_query_set().filter(highlighted=True).order_by('-highlight_priority')

class HighlighterMixin(models.Model):
    highlighted = models.BooleanField()
    highlight_priority = models.IntegerField(null=True, blank=True,
                choices=HIGHLIGHT_PRIORITY_CHOICES)
    objects = models.Manager()
    highlighteds = HighlightedManager()

    class Meta:
        abstract = True
