from django.test import TestCase
from .models import UserProfile

class UserProfileTestCase(TestCase):
    def setUp(self):
        UserProfile.objects.create(id=1041,username='222',activation_key='somewirdhash')          
        UserProfile.objects.create(id=1042,username='aa',activation_key='somewirdhash')        

    def test_user_profile_has_id(self):
        user = UserProfile.objects.get(id=1041)
        another = UserProfile.objects.get(id=1042)
        self.assertEqual(user.id,1041)
        self.assertEqual(another.id,1042)  
        user.delete() # Hust clean up
        another.delete()


if __name__=='__main__':
    unittest.main(warnings='ignore')

# Create your tests here.
