from django.test import TestCase
from .models import TestModel

class HighlighterTest(TestCase):
    def setUp(self):
        TestModel(name="test1", highlighted=True, highlight_priority=10).save()
        TestModel(name="test2", highlighted=True, highlight_priority=20).save()
        TestModel(name="test3", highlighted=False, highlight_priority=30).save()
        TestModel(name="test4", highlighted=False, highlight_priority=40).save()
        TestModel(name="test5", highlighted=True, highlight_priority=60).save()
        TestModel(name="test6", highlighted=True, highlight_priority=50).save()
        
    def test_list_highlighteds(self):
        highlighteds = [ x.name for x in TestModel.get_highlighteds() ]
        self.assertEqual(highlighteds, [ "test5", "test6", "test2", "test1" ])
