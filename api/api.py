from rest_framework import generics, permissions
from tastypie.resources import ModelResource
from models import UserProfile
from django.contrib.auth.models import User, AbstractUser
from tastypie.cache import SimpleCache
from tastypie import fields

class ProfileResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'profile'
        cache = SimpleCache(timeout=10)


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        cache = SimpleCache(timeout=10)

