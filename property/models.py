"""
 Property models
 Author: Dmitry Roitman
 2014
"""
from django.db import models
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.files.base import ContentFile
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.signals import pre_delete
from django.template.defaultfilters import slugify
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill
from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey
from django.utils.translation import ugettext as _
import twitter
"""
  Property thumbnail 
"""
class Thumbnail(ImageSpec):
    processors = [ResizeToFill(300, 150)]
    format = 'JPEG'
    options = {'quality': 60}

register.generator('myapp:thumbnail', Thumbnail)

"""
  Category model - RENT, SALE, FEATURED etc.
"""
@python_2_unicode_compatible
class Category(models.Model):
    category = models.CharField(max_length=30)
    def __unicode__(self):
        return unicode(self.category)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
 
    def __getitem__(self,items):
        return self.category

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('pl-category', args=[self.slug])

"""
  Rooms model - the number of rooms in a property or studio for zero - naming option
"""
@python_2_unicode_compatible
class Room(models.Model):
    rooms = models.CharField(max_length=30,blank=True, null=True)
    
    def __str__(self):
        return self.rooms

    def __unicode__(self):
        return unicode(self.rooms)

    def __getitem__(self,items):
        return self.rooms

    class Meta:
        verbose_name = 'bed rooms'
        verbose_name_plural = 'bed rooms'

"""
  Type model - Apartment Building, Coop, Condo, Parking Slot, Industrial Warehouse
"""
@python_2_unicode_compatible
class Type(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

    def __unicode__(self):
        return unicode(self.type)

    def __getitem__(self,items):
        return self.type


    class Meta:
        verbose_name = 'property type'
        verbose_name_plural = 'property types'
"""
  Borough model - can be used for any city with neighborhoods
"""
@python_2_unicode_compatible
class Borough(models.Model):
    borough = models.CharField(max_length=30)

    def __str__(self):
        return self.borough

    def __unicode__(self):
        return unicode(self.borough)

    def __getitem__(self,items):
        return self.borough

 
"""
  Neighborhood model - an arbitrary city neighborhood chained to borough
"""
@python_2_unicode_compatible
class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=30)
    borough = models.ForeignKey(Borough)
    class Meta:
        verbose_name = 'neighborhood'
        verbose_name_plural = 'neighborhoods'

    def __str__(self):
        return self.neighborhood

    def __unicode__(self):
        return unicode(self.neighborhood)

    def __getitem__(self,items):
        return self.neighborhood

"""
  Location model - a generalized type incluging borough and neighborhood
"""
@python_2_unicode_compatible
class Location(models.Model):
    borough = models.ForeignKey(Borough)
    neighborhood = ChainedForeignKey(Neighborhood, chained_field="borough", chained_model_field="borough")
    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'


    def __str__(self):
        return str(self.borough)+' - '+str(self.neighborhood)

    def __unicode__(self):
        return u'%s (%s)' % (str(self.borough)+' - '+str(self.neighborhood), self.url)


"""
  Property statuses - on sale, for rent, sold out etc.
"""
@python_2_unicode_compatible
class Status(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.status

    def __unicode__(self):
        return unicode(self.status)

    def __getitem__(self,items):
        return self.status
 

"""
  Property implementation - the basic model to list the properties
"""
@python_2_unicode_compatible
class Property(models.Model):

    property_id = models.IntegerField(blank=True, null=True, default=1)
    title = models.CharField(max_length=500)
    fulltitle = models.CharField(max_length=1600,blank=True, null=True)
    type = models.ForeignKey(Type)
    borough =  models.ForeignKey(Borough)
    neighborhood = ChainedForeignKey(Neighborhood, chained_field="borough", chained_model_field="borough")
    price = models.CharField(max_length=30)
    category  = models.ForeignKey(Category)
    size = models.CharField(max_length=30)
    rooms = models.ForeignKey(Room,blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=2400)
    published = models.DateTimeField("Date Published")
    expires = models.DateTimeField("Date expires")
    status = models.ForeignKey(Status)
    pets_allowed =  models.BooleanField(_('pets_allowed'),default=False)
    is_featured = models.BooleanField(_('is_featured'),default=False)
    pid = [property_id]
    property_url = _('properties/').join(str(pid))



    picture1 =  models.ImageField("Property View 1", upload_to="images/", 
                                  blank=True, null=True)
    picture2 =  models.ImageField("Property View 2", upload_to="images/", 
                                  blank=True, null=True)
    picture3 =  models.ImageField("Property View 3", upload_to="images/", 
                                  blank=True, null=True)
    picture4 =  models.ImageField("Property View 4", upload_to="images/", 
                                  blank=True, null=True)
    
    avatar_thumbnail = ImageSpecField(source='picture1',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'
        ordering = ('property_id',)

    def __str__(self):
        return self.title
        ordering = ('title', 'url',)

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.url)

    @models.permalink
    def get_absolute_url(self):
        return ('property_view', (), {'slug': self.slug}) 



"""
  Register the models with Dajngo Admin
"""

class RoomAdmin(admin.ModelAdmin):
    fiels = ('rooms')

class StatusAdmin(admin.ModelAdmin):
    fields = ('status')

class CategoryAdmin(admin.ModelAdmin):
    fields = ('category')

class TypeAdmin(admin.ModelAdmin):
    fields = ('type')

class BoroughAdmin(admin.ModelAdmin):
    fields = ('borough')

class NeighborhoodAdmin(admin.ModelAdmin):
    fields = ('neighborhood')

class LocationAdmin(admin.ModelAdmin):
    fields = ('location')

admin.site.register(Room)
admin.site.register(Type)
admin.site.register(Borough)
admin.site.register(Neighborhood)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Location)
