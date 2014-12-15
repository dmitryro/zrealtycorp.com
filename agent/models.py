from django.forms import Textarea
from django.db import models
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit



@python_2_unicode_compatible
class Role(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'role'
        verbose_name_plural = 'roles'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)

@python_2_unicode_compatible
class Agent(models.Model):
    title =  models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.ForeignKey(Role)
    phone =  models.CharField(max_length=30)
    email = models.EmailField()
    bio = models.TextField(max_length=500)
    avatar =  models.ImageField("Personal Avatar", upload_to="images/", blank=True, null=True)
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFit(180,180)],
                                      format='PNG',
                                      options={'quality': 80})

    class Meta:
        verbose_name = 'agent'
        verbose_name_plural = 'agents'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


    def get_absolute_url(self):
        return reverse('pl-agent', args=[self.slug])


class AgentAdmin(admin.ModelAdmin):
    fields = ('title','first_name','last_name','role','phone','email','bio','avatar')
    bio_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 6,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }

class RoleAdmin(admin.ModelAdmin):
    fields = ('role')

admin.site.register(Role)

# Create your models here.
