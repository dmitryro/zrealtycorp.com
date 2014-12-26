import os
import sys 
from django.test import TestCase
from .models import UserProfile
from zrealty import settings
from social_auth.tests.client import SocialClient
from oauth2client import gce
import httplib2

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

class GoogleOauthTestCase(TestCase):
    def setUp(self):

        self.client = SocialClient
        self.user = {
           'client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_CLIENT_ID,
           'secret': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
           'first_name': 'Dmitry',
           'last_name': 'Roitman',
           'username': 'dmitryro',
           'password': 'nu45edi1'
        }

    def test_google_login(self):

        credentials = gce.AppAssertionCredentials(
               scope='https://www.googleapis.com/auth/devstorage.read_write')
        http = credentials.authorize(httplib2.Http())

        print settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        print settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
        print settings.SOCIAL_AUTH_GOOGLE_OAUTH2_CLIENT_ID

if __name__=='__main__':
    unittest.main(warnings='ignore')

# Create your tests here.
