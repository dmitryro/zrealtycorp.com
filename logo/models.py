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
class Logo(models.Model):
    title =  models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    url =  models.ImageField("Corporate Logo", upload_to="images/", blank=True, null=True)
    height = models.IntegerField()
    width = models.IntegerField()
    slogan = models.CharField(max_length=300)
    logo_thumbnail = ImageSpecField(source='url',
                                      processors=[ResizeToFit(230,58)],
                                      format='PNG',
                                      options={'quality': 80})
    class Meta:
        verbose_name = 'logo'
        verbose_name_plural = 'logos'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)



class LogoAdmin(admin.ModelAdmin):
    fields = ('title','version','slogan','url','height','width')


admin.site.register(Logo)

