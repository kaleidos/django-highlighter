from django.db import models
from .settings import *

PRIORITY_CHOICES = [ (x,x) for x in range(*HIGHLIGHTER_PRIORITY_RANGE) ]


class HighlightedManager(models.Manager):
    def get_query_set(self):
        return super(HighlightedManager, self).get_query_set().filter(is_highlighted=True).order_by('-priority')


class PrioritizedManager(models.Manager):
    def get_query_set(self):
        return super(PrioritizedManager, self).get_query_set().all().order_by('-is_highlighted','-priority')


class HighlighterMixin(models.Model):
    is_highlighted = models.BooleanField()
    priority = models.IntegerField(null=True, blank=True,
                choices=PRIORITY_CHOICES)
    objects = models.Manager()
    highlighted_objects = HighlightedManager()
    prioritized_objects = PrioritizedManager()

    class Meta:
        abstract = True
