from rest_framework import serializers
from utils.models import Member, Login
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    type = serializers.CharField(max_length=30)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.user = attrs.get('user', instance.user)
            return instance
        return Type(**attrs)


class MemberSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    category = serializers.CharField(max_length=30)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.category = attrs.get('member', instance.member)
            return instance
        return Member(**attrs)




