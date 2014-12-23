from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


"""
  User Profile in Dashboard
"""
@python_2_unicode_compatible
class UserProfile(models.Model):

    user = models.OneToOneField(User) 
    username = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    confirm = models.CharField(max_length=20, blank=True)
    first = models.CharField(max_length=50, blank=True)
    last = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    phone = models.CharField(max_length=50, blank=True)     
    avatar =  models.ImageField("Avatar", upload_to="images/",
                                  blank=True, null=True)
    bio = models.TextField(max_length=2400)

    def __str__(self):
        return self.user_id

    def __unicode__(self):
        return self.user_id

    class Meta:
        verbose_name_plural=u'User profiles'


"""
  Friend List - a list of friends of the user in Dashboard
"""
@python_2_unicode_compatible
class FriendList(models.Model):
    title = models.CharField(max_length=50, blank=True)
    owner = models.OneToOneField(UserProfile)

    def __str__(self):
        return self.nickname

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name_plural=u'Friends'

"""
  Friend - a Member of the Friend List in Dashboard
"""
@python_2_unicode_compatible
class Friend(models.Model):
    nickname = models.CharField(max_length=20)
    list = models.ForeignKey(FriendList,default=None,blank=True)
    def __str__(self):
        return self.nickname

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name_plural=u'Friends'


"""
  PrivateMessage in Dashboard
"""
@python_2_unicode_compatible
class PrivateMessage(models.Model):
    author = models.OneToOneField(UserProfile, blank=True)
    receiver = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=2400)
  

    def __str__(self):
        return self.author.username

    def __unicode__(self):
        return self.author.username

    class Meta:
        verbose_name_plural=u'Private Message'
    

 
