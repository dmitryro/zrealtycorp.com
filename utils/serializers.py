from rest_framework import serializers
from utils.models import Member, Login
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ('username','password')

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('username','email', 'password','who_are_you')


