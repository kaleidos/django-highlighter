from django.db import models
from ..models import HighlighterMixin

class TestModel(HighlighterMixin, models.Model):
    name = models.CharField(max_length=10)
