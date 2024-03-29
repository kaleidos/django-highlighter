Django Highlighter
==================

Django highlighter is an app to highlight and/or prioritise objects in your app.

Configuration
-------------

Adding it to installed apps is not necesary.

You can configure the "range" of posible priority values with the 
HIGHLIGHTER_PRIORITY_RANGE setting, for example:

HIGHLIGHTER_PRIORITY_RANGE = [1,10]

Internally it's execute the range function, then [1, 10] means >= 1 and < 10.

Usage
-----

To use django-highlighter you only have to add the HighlighterMixin to your
models, and this will add 2 fields highlighted (boolean) and highlight_priority
(integer). You can use this fields directly or use the Model.highlighted_objects
and/or Model.prioritized_objects managers.

Example
-------

::

  class Article(HighlighterMixin, models.Model):
      title = models.CharField(max_length=150)
      publication_date = models.DateTimeField()

  highlighted_articles = Article.highlighted_objects.all()
  all_prioritized_articles = Article.prioritized_objects.order_by('-publication_date')
