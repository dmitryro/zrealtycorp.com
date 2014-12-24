from rest_framework import generics, permissions
from tastypie.resources import ModelResource
from models import UserProfile
from tastypie.cache import SimpleCache
from tastypie import fields

class ProfileResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'profile'
        cache = SimpleCache(timeout=10)
