from django.db import models
from django.contrib.auth.models import User, AbstractUser
import hashlib, datetime, random
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.encoding import python_2_unicode_compatible
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@python_2_unicode_compatible
class UserProfile(models.Model):
    username = models.CharField(max_length=140, blank=True)
    activation_key = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.type

    def __unicode__(self):
        return unicode(self.type)

    def __getitem__(self,items):
        return self.type

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'


