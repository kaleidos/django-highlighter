Django Highlighter
==================

Django highlighter is an app to highlight objects in your app, and give it a
priority.

Configuration
-------------

Adding it to installed apps is not necesary.

You can configure the "range" of posible priority values with the HIGHLIGHTER_PRIORITY_RANGE setting, for example:

HIGHLIGHTER_PRIORITY_RANGE = [1,10]

Internally it's execute the range function, then [1, 10] means >= 1 and < 10.

Usage
-----

To use django-highlighter you only have to add the HighlighterMixin to your
models, and this will add 2 fields highlighted (boolean) and highlight_priority
(integer). You can use this fields directly or use the Model.highlighteds
manager.
