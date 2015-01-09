from django.db import models
# Create your models here.

from django.forms import Textarea
from django.db import models
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


# Create your models here.
@python_2_unicode_compatible
class Icon(models.Model):
    title =  models.CharField(max_length=30)
    icon=  models.ImageField("Menu Icon", upload_to="images/", blank=True, null=True)
    height = models.IntegerField()
    width = models.IntegerField()
    url = models.CharField(max_length=500, blank=True, null=True)
    icon_thumbnail = ImageSpecField(source='icon',
                                      processors=[ResizeToFit(50,50)],
                                      format='PNG',
                                      options={'quality': 80})
    class Meta:
        verbose_name = 'icon'
        verbose_name_plural = 'icons'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


# Create your models here.
@python_2_unicode_compatible
class SocialAuthIcon(models.Model):
    title =  models.CharField(max_length=30)
    icon=  models.ImageField("Social Authentication Icon", upload_to="images/", blank=True, null=True)
    height = models.IntegerField()
    width = models.IntegerField()
    url = models.CharField(max_length=500, blank=True, null=True)
    icon_thumbnail = ImageSpecField(source='icon',
                                      processors=[ResizeToFit(40,40)],
                                      format='PNG',
                                      options={'quality': 40})
    class Meta:
        verbose_name = 'Social Authentication Icon'
        verbose_name_plural = 'Social Authentication Icons'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


@python_2_unicode_compatible
class SocialIcon(models.Model):
    title =  models.CharField(max_length=30)
    icon=  models.ImageField("Social Icon", upload_to="images/", blank=True, null=True)
    height = models.IntegerField()
    width = models.IntegerField()
    url = models.CharField(max_length=500, blank=True, null=True)
    icon_thumbnail = ImageSpecField(source='icon',
                                      processors=[ResizeToFit(50,50)],
                                      format='PNG',
                                      options={'quality': 80})
    class Meta:
        verbose_name = 'social icon'
        verbose_name_plural = 'social icons'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


@python_2_unicode_compatible
class ActionIcon(models.Model):
    action_id = models.CharField(max_length=30, blank=True, null=True)
    title =  models.CharField(max_length=30)
    icon=  models.ImageField("Action Icon", upload_to="images/", blank=True, null=True)
    height = models.IntegerField()
    width = models.IntegerField()
    url = models.CharField(max_length=500, blank=True, null=True)
    icon_thumbnail = ImageSpecField(source='icon',
                                      processors=[ResizeToFit(50,50)],
                                      format='PNG',
                                      options={'quality': 80})
    class Meta:
        verbose_name = 'action icon'
        verbose_name_plural = 'action icons'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


"""
  Register with admin
"""
class ActionIconAdmin(admin.ModelAdmin):
    fields = ('action_id','title','icon','url','height','width')

class SocialIconAdmin(admin.ModelAdmin):
    fields = ('title','icon','url','height','width')

class IconAdmin(admin.ModelAdmin):
    fields = ('title','icon','url','height','width')

class SocialAuthIconAdmin(admin.ModelAdmin):
    fields = ('title','icon','url','height','width')


admin.site.register(Icon)
admin.site.register(SocialIcon)
admin.site.register(ActionIcon)
admin.site.register(SocialAuthIcon)
