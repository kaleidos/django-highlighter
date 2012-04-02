from django.test import TestCase
from .models import TestModel

class HighlighterTest(TestCase):
    def setUp(self):
        TestModel.objects.create(name="test1", is_highlighted=True,  priority=10)
        TestModel.objects.create(name="test2", is_highlighted=True,  priority=20)
        TestModel.objects.create(name="test3", is_highlighted=False, priority=30)
        TestModel.objects.create(name="test4", is_highlighted=False, priority=40)
        TestModel.objects.create(name="test5", is_highlighted=True,  priority=60)
        TestModel.objects.create(name="test6", is_highlighted=True,  priority=50)
        
    def test_list_highlightes(self):
        highlighted_list = [ x.name for x in TestModel.highlighted_objects.all() ]
        self.assertEqual(highlighted_list, ["test5", "test6", "test2", "test1"])
    
    def test_list_prioritizes(self):
        prioritized_list = [ x.name for x in TestModel.prioritized_objects.all() ]
        self.assertEqual(prioritized_list, ["test5", "test6", "test2", "test1", "test4", "test3"])
