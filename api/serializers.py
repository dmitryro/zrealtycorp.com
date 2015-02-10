from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import UserProfile
import json


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.Field()

    class Meta:
        model = UserProfile
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.id = validated_data.get('id', instance.id)
            instance.save()
            return instance
        return UserProfile(**attrs)

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(UserProfileSerializer, self).to_representation(self)
           ret['id']= instance.id
           return ret


