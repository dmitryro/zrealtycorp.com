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
"""
Property thumbnail
"""
class Thumbnail(ImageSpec):
    processors = [ResizeToFill(300, 150)]
    format = 'JPEG'
    options = {'quality': 60}


class MaintenancePage(models.Model):
    title = models.CharField(max_length=200)
    memo =  models.CharField(max_length=500) 
    down_since = models.DateTimeField("Down since")
    down_until = models.DateTimeField("Down until")
    avatar = models.ImageField("Avatar", upload_to="images/",
                               blank=True, null=True)
    contact = models.CharField(max_length=200)


class FrontPage(models.Model):
    title = models.CharField(max_length=200)
    note  =  models.CharField(max_length=200)


class SalesPage(models.Model):
    title = models.CharField(max_length=200)
    note  =  models.CharField(max_length=200)


class RentPage(models.Model):
    title = models.CharField(max_length=200)
    note  =  models.CharField(max_length=200)


class ContactPage(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    email =  models.EmailField(max_length=30)
    subject =  models.CharField(max_length=30)
    message = models.CharField(max_length=500)


class MaintenancePageAdmin(admin.ModelAdmin):
    fields = ('title','memo','down_since','down_until','contact')


class FrontPageAdmin(admin.ModelAdmin):
    fields = ('title','note')


class SalesPageAdmin(admin.ModelAdmin):
    fields = ('title','note')


class RentPageAdmin(admin.ModelAdmin):
    fields = ('title','note')


class ContactAdmin(admin.ModelAdmin):
    fields = ('title','name','email','subject','message')


admin.site.register(MaintenancePage)
admin.site.register(FrontPage)
admin.site.register(SalesPage)
admin.site.register(RentPage)
admin.site.register(ContactPage)
# Create your models here.
