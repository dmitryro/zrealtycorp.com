from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from models import Status, Type, Category, Room

# Create your tests here.
def setUp(self):
    pass


def tearDown(self):
    pass

class PropertyTest(TestCase):
    def test_serialization(self):
        pass



class StatusTestCase(TestCase):
    
    def setUp(self):
        st = Status.objects.create(status='mock')

    def tearDown(self):
        pass
 
    def test_status_creation(self):
        status = Status.objects.get(status='mock')
        self.assertEqual(status.status,'mock')
        status.delete() # Hust clean up

class StatusTestCase(TestCase):

    def setUp(self):
        st = Status.objects.create(status='mock')

    def tearDown(self):
        pass

    def test_status_creation(self):
        status = Status.objects.get(status='mock')
        self.assertEqual(status.status,'mock')
        status.delete() # Hust clean up

class TypeTestCase(TestCase):

    def setUp(self):
        st = Type.objects.create(type='mock')

    def tearDown(self):
        pass

    def test_type_creation(self):
        type = Type.objects.get(type='mock')
        self.assertEqual(type.type,'mock')
        type.delete() # Hust clean up


class CategoryTestCase(TestCase):

    def setUp(self):
        st = Category.objects.create(category='mock')

    def tearDown(self):
        pass

    def test_category_creation(self):
        category = Category.objects.get(category='mock')
        self.assertEqual(category.category,'mock')
        category.delete() # Hust clean up



if __name__=='__main__':
    unittest.main(warnings='ignore')

