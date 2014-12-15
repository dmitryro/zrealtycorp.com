from django.forms import widgets
from rest_framework import serializers
from models import Property, Room, Category, Neighborhood, Borough, Type, Status

class BoroughSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    borough = serializers.CharField(max_length=30,read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.borough = attrs.get('borough', instance.borough)
            return instance
        return Borough(**attrs)

class NeighborhoodSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    neighborhood = serializers.CharField(max_length=30,read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.neighborhood = attrs.get('neighborhood', instance.neighborhood)
            return instance
        return Neighborhood(**attrs)

class CategorySerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    category = serializers.CharField(max_length=30,read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.category = attrs.get('category', instance.category)
            return instance
        return Category(**attrs)

class RoomsSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    rooms = serializers.CharField(max_length=30,read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.category = attrs.get('rooms', instance.rooms)
            return instance
        return Room(**attrs)


class TypeSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    type = serializers.CharField(max_length=30,read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.category = attrs.get('type', instance.type)
            return instance
        return Type(**attrs)

class StatusSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    status = serializers.CharField(max_length=30,read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.category = attrs.get('status', instance.status)
            return instance
        return Status(**attrs)



class PropertySerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    property_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=30,read_only=True)
    category  = serializers.RelatedField(many=False,read_only=True)
    type  = serializers.RelatedField(many=False,read_only=True)
    status  = serializers.RelatedField(many=False,read_only=True)
    neighborhood  = serializers.RelatedField(many=False,read_only=True)
    borough = serializers.RelatedField(many=False,read_only=True)
    price = serializers.CharField(max_length=30,read_only=True)
    size = serializers.CharField(max_length=30,read_only=True)
    rooms =  serializers.CharField(max_length=30,read_only=True)
    bathrooms = serializers.CharField(max_length=30,read_only=True)
    pets_allowed =  serializers.BooleanField(default=False,read_only=True)
    is_featured = serializers.BooleanField(default=False,read_only=True)
    property_url = serializers.CharField(max_length=200,read_only=True)
    description = serializers.CharField(max_length=500,read_only=True)
    published = serializers.DateTimeField(read_only=True)
    expires = serializers.DateTimeField(read_only=True)
    picture1 =  serializers.ImageField(read_only=True)
    picture2 =  serializers.ImageField(read_only=True)
    picture3 =  serializers.ImageField(read_only=True)
    picture4 =  serializers.ImageField(read_only=True)
    avatar_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Property
        fields = ('property_id', 'title', 'category', 'type', 'status', 'neighborhood', 
                  'borough', 'price', 'size', 'rooms', 'bathrooms','pets_allowed','is_featured',
                  'property_url', 'picture1', 'picture2', 'picture3','picture4', 'avatar_thumbnail',
                  'published','expires','description')

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.property_id = attrs.get('property_id', instance.property_id)
            instance.title = attrs.get('title', instance.title)
            instance.category = attrs.get('category', instance.category)
            instance.type = attrs.get('type', instance.type)
            instance.neighborhood = attrs.get('neighborhood', instance.neigborhood)
            instance.borough = attrs.get('borough', instance.borough)
            instace.price = attrs.get('price', instance.price)
            instance.size = attrs.get('size', instance.size)
            instance.rooms = attrs.get('rooms', instance.rooms)
            instance.bathrooms = attrs.get('bathrooms', instance.bathrooms)
            instance.pets_allowed = attrs.get('pets_allowed', instance.pets_allowed)
            instance.is_featured = attrs.get('is_featured', instance.is_featured)  
            instance.property_url = attrs.get('property_url', instance.property_url)
            instance.published = attrs.get('published', instance.published)
            instance.expires = attrs.get('expires', instance.expires)
            instance.description = attrs.get('description', instance.description)
            instance.picture1 = attrs.get('picture1', instance.picture1)
            instance.picture2 = attrs.get('picture2', instance.picture2)
            instance.picture3 = attrs.get('picture3', instance.picture3)
            instance.picture4 = attrs.get('picture4', instance.picture4)
            instance.avatar_thumbnail = attrs.get('avatar_thumbnail', instance.avatar_thumbnail)
            return instance

        return Property(**attrs)

class AgentSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.

    def restore_object(self, attrs, instance=None):pass


