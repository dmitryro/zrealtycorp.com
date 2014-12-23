from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import UserProfile
import json


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    username = serializers.CharField(max_length=140,read_only=True)
    activation_key = serializers.CharField(max_length=140,read_only=True)

    class Meta:
        model = UserProfile
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.username = validated_data.get('username', instance.username)
            instance.activation_key = validated_data.get('activation_key', instance.activation_key)
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
           ret['username']= instance.username
           ret['activation_key']= instance.activation_key
           return ret

