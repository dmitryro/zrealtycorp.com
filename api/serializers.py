from django.contrib.auth.models import User, Group
from property.models import Property
from rest_framework import serializers

class PropertySerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    type = serializers.CharField(required=False,
                                  max_length=100)

    class Meta:
        model = Property
        fields = ('type', 'borough', 'neighborhood','price')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
