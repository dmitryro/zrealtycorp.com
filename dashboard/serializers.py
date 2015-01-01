from django.contrib.auth.models import User, AbstractUser
from rest_framework import serializers
from dashboard.models import Post, Thread, Comment, Property

class PostSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    author = serializers.CharField(max_length=150,read_only=True)
    link = serializers.CharField(max_length=150,read_only=True)     
    title = serializers.CharField(max_length=150,read_only=True)    
    post = serializers.CharField(max_length=500,read_only=True)
    published = serializers.CharField(max_length=300,read_only=True)

    class Meta:
        model = Post
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.author = validated_data.get('author', instance.author)
            instance.link = validated_data.get('link', instance.link)
            instance.title = validated_data.get('title', instance.link)
            instance.post = validated_data.get('post', instance.post)
            instance.published = validated_data.get('published', instance.published)
            instance.id = validated_data.get('id', instance.id)
            instance.save()
            return instance
        return Post(**attrs)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(PostSerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['author']= instance.author
           ret['title']= instance.title 
           ret['post']= instance.post
           ret['published']= instance.published
           return ret


class CommentSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    comment = serializers.CharField(max_length=100)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.comment = attrs.get('comment', instance.comment)
            return instance
        return Comment(**attrs)

class ThreadSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    thread = serializers.CharField(max_length=100)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.thread = attrs.get('thread', instance.thread)
            return instance
        return Thread(**attrs)

class PropertySerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    property = serializers.CharField(max_length=100)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.property = attrs.get('property', instance.property)
            return instance
        return Property(**attrs)

class UserSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    username = serializers.CharField(max_length=150,read_only=True)
    password = serializers.CharField(max_length=150,read_only=True)
    email = serializers.EmailField(max_length=150,read_only=True)
    first_name = serializers.CharField(max_length=500,read_only=True)
    last_name = serializers.CharField(max_length=300,read_only=True)

    class Meta:
        model = User
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.username= validated_data.get('username', instance.username)
            instance.password = validated_data.get('password', instance.password)
            instance.email = validated_data.get('email', instance.email)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.id = validated_data.get('id', instance.id)
            instance.save()
            return instance
        return User(**attrs)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(UserSerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['username']= instance.username
           ret['password']= instance.password
           ret['email']= instance.email
           ret['first_name']= instance.first_name
           ret['last_name']= instance.last_name
           return ret

