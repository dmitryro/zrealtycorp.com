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
  FriendLists in Dashboard
"""
@python_2_unicode_compatible
class FriendList(models.Model):
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.owner.username

    def __unicode__(self):
        return self.owner.username

    class Meta:
        verbose_name_plural=u'List owner'

