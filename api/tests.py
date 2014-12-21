from django.test import TestCase
from api.models import UserProfile

class UserProfileTestCase(TestCase):
    def setUp(self):
        UserProfile.objects.create(user_id=1041,activation_key='somewirdhash')          UserProfile.objects.create(user_id=1042,activation_key='somewirdhash')        
    def test_user_profile_has_id(self):
         user = UserProfile.objects.get(user_id=1041)
         another = UserProfile.objects.get(user_id=1041)
         self.assertEqual(user.user_id,1041)
         self.assertEqual(another.user_id,1042)  

if __name__=='__main__':
    unittest.main(warnings='ignore')

# Create your tests here.
