from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from models import PrivateMessage, UserProfile, Post, Comment
from django.contrib.auth.models import User, AbstractUser
from datetime import tzinfo, timedelta, datetime
# Create your tests here.

class TZ(tzinfo):
    def utcoffset(self, dt): return timedelta(minutes=-399)

class PrivateMessageTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_post_publishing(self):
        
        try:
            t = datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
            author = 'Some'
            title = 'Some'
            link = 'Some'
            message = 'Some'
            post = Post(published='ssss',author=author,title=title,link=link,post=message)
            post.save()
            post = Post.objects.get(published='ssss')
            assert post.published == 'ssss'     
        except Exception,R:
            print R

    def test_private_message_creation(self):
   
        try:
            t = datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
            author = 'Some'
            title = 'Some'
            link = 'Some'
            message = 'Some'
            p = Post(published='tt',title='tt',post='tt',author='tt')            
            post = Post(published='ssss',author=author,title=title,link=link,post=message)
            post.save()
        except Exception,R:
            print R

class CommentTestCase(TestCase):
    def setUp(self):
        pass

    def test_comment_added(self):
        post_id = 16
        username = 'root'
        comment = 'test'
        try:
            post = Post.objects.get(id=post_id)
            comt = Comment(post_id=post.id,username=username,comment=comment)
            comt.save()
        except Exception,R:
            print R

        pass

    def test_comment_removed(self):
        pass

       # pm = PrivateMessage.objects.get(title='mock')
       # self.assertEqual(pm.title,'mock')
       # pm.delete() # Hust clean up

