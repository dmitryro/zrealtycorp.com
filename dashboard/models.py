from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect, HttpResponse
from django.template.defaultfilters import slugify
from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey
from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from property.models import Type, Borough, Neighborhood, Category, Status, Room 

"""
  Property thumbnail
"""
class Thumbnail(ImageSpec):
    processors = [ResizeToFill(300, 150)]
    format = 'JPEG'
    options = {'quality': 60}

register.generator('dashboard:thumbnail', Thumbnail)

class ImageWithThumbnail(models.Model):
     name = models.CharField(max_length = 255)

     image = models.ImageField(upload_to='images/',max_length=500,blank=True,null=True)
     thumbnail = models.ImageField(upload_to='iamges/',max_length=500,blank=True,null=True)

     def create_thumbnail(self):
         # original code for this method came from
         # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

         # If there is no image associated with this.
         # do not create thumbnail
         if not self.image:
             return

         from PIL import Image
         from cStringIO import StringIO
         from django.core.files.uploadedfile import SimpleUploadedFile
         import os

         # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (200,200)

         DJANGO_TYPE = self.image.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

         # Open original photo which we want to thumbnail using PIL's Image
         image = Image.open(StringIO(self.image.read()))

         # Convert to RGB if necessary
         # Thanks to Limodou on DjangoSnippets.org
         # http://www.djangosnippets.org/snippets/20/
         #
         # I commented this part since it messes up my png files
         #
         #if image.mode not in ('L', 'RGB'):
         #    image = image.convert('RGB')

         # We use our PIL Image object to create the thumbnail, which already
         # has a thumbnail() convenience method that contrains proportions.
         # Additionally, we use Image.ANTIALIAS to make the image look better.
         # Without antialiasing the image pattern artifacts may result.
         image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

         # Save the thumbnail
         temp_handle = StringIO()
         image.save(temp_handle, PIL_TYPE)
         temp_handle.seek(0)

         # Save image to a SimpleUploadedFile which can be saved into
         # ImageField
         suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
         # Save SimpleUploadedFile into image field
         self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

     def save(self):
         # create a thumbnail
         self.create_thumbnail()

         super(ImageWithThumbnail, self).save()

"""
  User Profile in Dashboard
"""
@python_2_unicode_compatible
class UserProfile(models.Model):

    user = models.OneToOneField(User) 
    username = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    confirm = models.CharField(max_length=20, blank=True)
    first = models.CharField(max_length=50, blank=True)
    last = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    phone = models.CharField(max_length=50, blank=True)     
    avatar =  models.ImageField("Avatar", upload_to="images/",
                                  blank=True, null=True)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.user_id

    def __unicode__(self):
        return self.user_id

    class Meta:
        verbose_name_plural=u'User profiles'



"""
  PrivateMessage in Dashboard
"""
@python_2_unicode_compatible
class PrivateMessage(models.Model):
    author = models.OneToOneField(UserProfile, blank=True)
    receiver = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)
    image =  models.ImageField("Image", upload_to="images/",
                                  blank=True, null=True)
    thumbnail = models.ImageField(upload_to='iamges/',max_length=500,blank=True,null=True)

    def create_thumbnail(self):
         # original code for this method came from
         # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

         # If there is no image associated with this.
         # do not create thumbnail
         if not self.image:
             return

         from PIL import Image
         from cStringIO import StringIO
         from django.core.files.uploadedfile import SimpleUploadedFile
         import os

         # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (200,200)

         DJANGO_TYPE = self.image.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

         # Open original photo which we want to thumbnail using PIL's Image
         image = Image.open(StringIO(self.image.read()))

         # Convert to RGB if necessary
         # Thanks to Limodou on DjangoSnippets.org
         # http://www.djangosnippets.org/snippets/20/
         #
         # I commented this part since it messes up my png files
         #
         #if image.mode not in ('L', 'RGB'):
         #    image = image.convert('RGB')

         # We use our PIL Image object to create the thumbnail, which already
         # has a thumbnail() convenience method that contrains proportions.
         # Additionally, we use Image.ANTIALIAS to make the image look better.
         # Without antialiasing the image pattern artifacts may result.
         image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

         # Save the thumbnail
         temp_handle = StringIO()
         image.save(temp_handle, PIL_TYPE)
         temp_handle.seek(0)

         # Save image to a SimpleUploadedFile which can be saved into
         # ImageField
         suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
         # Save SimpleUploadedFile into image field
         self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)
    def save(self):
         # create a thumbnail
         self.create_thumbnail()

         super(ImageWithThumbnail, self).save()


    message = models.TextField(max_length=200)
  

    def __str__(self):
        return self.author.username

    def __unicode__(self):
        return self.author.username

    class Meta:
        verbose_name_plural=u'Private Message'
    


"""
  PrivateMessage in Dashboard
"""
@python_2_unicode_compatible
class Property(models.Model):
    publisher = models.OneToOneField(UserProfile,default=0, blank=True)
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=30)
    category = models.ForeignKey(Category,related_name='dashboard_category')
    location = models.CharField(max_length=200)
    rooms = models.ForeignKey(Room,related_name='dashboard_rooms')
    price = models.CharField(max_length=30)
  

    image =  models.ImageField("Image", upload_to="images/",
                                  blank=True, null=True)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

    description = models.TextField(max_length=1200)


    def __str__(self):
        return self.publisher.username

    def __unicode__(self):
        return self.publiser.username

    class Meta:
        verbose_name_plural=u'Property'


"""
 Initiate a new thread or use existing one
"""
@python_2_unicode_compatible
class Thread(models.Model):
   name = models.CharField(max_length=150)
   published = models.DateTimeField("Date Published")

   def __str__(self):
       return self.name

   def __unicode__(self):
       return self.name

   class Meta:
       verbose_name_plural=u'Threads'


"""
 Post into one of the threads
"""
@python_2_unicode_compatible
class Post(models.Model):
   published = models.CharField(max_length=150)
   author = models.CharField(max_length=150, blank=True)
   title = models.CharField(max_length=150)
   link =  models.CharField(max_length=550) 
   post = models.TextField(max_length=400)
  
   def __str__(self):
       return self.title

   def __unicode__(self):
       return self.title

   class Meta:
       verbose_name_plural=u'Posts'
 
