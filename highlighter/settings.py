from django.conf import settings

HIGHLIGHTER_PRIORITY_RANGE = getattr(settings, 'HIGHLIGHTER_PRIORITY_RANGE', [1,100])
