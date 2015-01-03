import os
import sys 
from django.test import TestCase
from .models import UserProfile
from dashboard.models import Post, Comment
from zrealty import settings
from social_auth.tests.client import SocialClient
from oauth2client import gce
from oauth2client import client
from oauth2client.client import OAuth2WebServerFlow
import httplib2
import oauth.oauth as oauth
import gdata.gauth
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.test import APIClient
from rest_framework.response import Response



SERVER = 'localhost'
PORT = 8080

# fake urls for the test server (matches ones in server.py)
REQUEST_TOKEN_URL = 'https://photos.example.net/request_token'
ACCESS_TOKEN_URL = 'https://photos.example.net/access_token'
AUTHORIZATION_URL = 'https://photos.example.net/authorize'
CALLBACK_URL = 'http://printer.example.com/request_token_ready'
RESOURCE_URL = 'http://photos.example.net/photos'


   
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

class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_authentication(self):
        client = APIClient()
        res = client.login(username='roota', password='nu45edi')
        print res

class GoogleOauthTestCase(TestCase):
    def setUp(self):

        self.client = SocialClient

    def test_google_login(self):
        client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_CLIENT_ID
        client_secret = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
        consumer = oauth.OAuthConsumer(client_id, client_secret)
        token = oauth.OAuthToken(client_id, client_secret)
        signature_method_plaintext = oauth.OAuthSignatureMethod_PLAINTEXT()
        signature_method_hmac_sha1 = oauth.OAuthSignatureMethod_HMAC_SHA1()

        flow = OAuth2WebServerFlow(client_id=client_id,
                                   client_secret=client_secret,
                                   scope='https://www.googleapis.com/auth/calendar',
                                   redirect_uri='http://example.com/auth_return')
        #auth_uri = flow.step1_get_authorize_url()
        #print auth_uri
        print token
        #print settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        #print settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
        #print settings.SOCIAL_AUTH_GOOGLE_OAUTH2_CLIENT_ID

if __name__=='__main__':
    unittest.main(warnings='ignore')

# Create your tests here.
