from collections import OrderedDict
from django.forms import widgets
from rest_framework import serializers
from models import Property, Room, Category, Neighborhood, Borough, Type, Status
import json

class BoroughSerializer(serializers.Serializer):
    id = serializers.Field()
    borough = serializers.CharField(max_length=30,read_only=True)

    class Meta:
        model = Borough
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.borough = validated_data.get('borough', instance.borough)
            instance.id = validated_data.get('id', instance.id)
            instance.save()
            return instance
        return Borough(**attrs)

    def create(self, validated_data):
        return Borough.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(BoroughSerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['borough']= instance.borough
           return ret


class NeighborhoodSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    neighborhood = serializers.CharField(max_length=30,read_only=True)

    class Meta:
        model = Neighborhood
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.neighborhood = validated_data.get('neighborhood', instance.neighborhood)
            instance.id = validated_data.get('id', instance.id)
            instance.save()
            return instance
        return Neighborhood(**attrs)

    def create(self, validated_data):
        return Neighborhood.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(NeighborhoodSerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['neighborhood']= instance.neighborhood
           return ret


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.Field()
    category = serializers.CharField(max_length=30,read_only=True)

    class Meta:
        model = Category
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.category = validated_data.get('category', instance.category)
            instance.id = validated_data.get('id', instance.id)  
            instance.save()
            return instance
        return Category(**attrs)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(CategorySerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['category']= instance.category
           return ret


class RoomsSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    rooms= serializers.CharField(max_length=30,read_only=True)

    class Meta:
        model = Room
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.rooms = validated_data.get('rooms', instance.rooms)
            instance.id = validated_data.get('id', instance.id)
            instance.save()
            return instance
        return Room(**attrs)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(RoomsSerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['rooms']= instance.rooms
           return ret


class TypeSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    type = serializers.CharField(max_length=30,read_only=True)

    class Meta:
        model = Type
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.id = validated_data.get('id', instance.id)
            instance.type = validated_data.get('type',instance.type)
            instance.save()
            return instance
        return Type(**attrs)

    def create(self, validated_data):
        return Type.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(TypeSerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['type']= instance.type
           return ret


class StatusSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    type = serializers.CharField(max_length=30,read_only=True)

    class Meta:
        model = Status
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.id = validated_data.get('id', instance.id)
            instance.status = validated_data.get('status',instance.status)
            instance.save()
            return instance
        return Status(**attrs)

    def create(self, validated_data):
        return Status.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(StatusSerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['status']= instance.status
           return ret


class PropertySerializer(serializers.ModelSerializer):
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    def to_representation(self, instance):
        if instance:
            ret = super(PropertySerializer, self).to_representation(self)
            ret['title']=instance.title
            ret['property_id']=instance.property_id
            ret['category']= instance.category['category']
            ret['type']=instance.type['type']
            ret['status']=instance.status['status']
            ret['neighborhood']=instance.neighborhood['neighborhood']
            ret['borough']=instance.borough['borough']
            ret['price']=instance.price
            ret['size']=instance.size  
            ret['rooms']=instance.rooms['rooms']
            ret['bathrooms']=instance.bathrooms
            ret['pets_allowed']=instance.pets_allowed
            ret['is_featured']=instance.is_featured
            ret['property_url']=instance.property_url
            ret['description']=instance.description
            ret['published']=instance.published
            ret['expires']=instance.published
            ret['picture1']=instance.picture1.name  
            ret['picture2']=instance.picture2.name
            ret['picture3']=instance.picture3.name
            ret['picture4']=instance.picture4.name
            ret['avatar_thumbnail']=instance.avatar_thumbnail.name
            return ret

    class Meta:
        model = Property
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.property_id = validated_data.get('property_id', instance.property_id)
            instance.title = validated_data.get('title', instance.title)
            instance.category = validated_data.get('category', instance.category)
            instance.type = validated_data.get('type', instance.type)
            instance.borough = validated_data.get('borough', instance.borough) 
            instance.neighborhood = validated_data.get('neighborhood', instance.neighborhood)
            instance.price = validated_data.get('price', instance.price)
            instance.size = validated_data.get('size', instance.size)
            instance.rooms = validated_data.get('rooms', instance.rooms)
            instance.bathrooms = validated_data.get('bathrooms', instance.bathrooms)
            instance.pets_allowed = validated_data.get('pets_allowed', instance.pets_allowed)
            instance.is_featured = validated_data.get('is_featured', instance.is_featured)
            instance.property_url = validated_data.get('property_url', instance.property_url)
            instance.description = validated_data.get('description', instance.description)   
            instance.published = validated_data.get('published', instance.published)
            instance.expires = validated_data.get('expires', instance.expires)
            instance.picture1 = validated_data.get('picture1',instance.picture1)
            instance.picture2 = validated_data.get('picture2',instance.picture2) 
            instance.picture3 = validated_data.get('picture3',instance.picture3) 
            instance.picture4 = validated_data.get('picture4',instance.picture4)
            instance.avatar_thumbnail = validated_data.get('avatar_thumbnail',instance.avatar_thumbnail)
            instance.save()
            return instance
        return Property(**attrs)

    def create(self, validated_data):
        return Property.objects.create(**validated_data)



class AgentSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.

    def restore_object(self, attrs, instance=None):pass


