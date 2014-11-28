from django.db import models
from django.contrib import admin
from django import forms
# This model is for basic html meta settings
class ContactMetaProp(models.Model):
    title = models.CharField(max_length=150)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150,blank=True, null=True)
    city =  models.CharField(max_length=150)
    zip = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    hours = models.CharField(max_length=200)
    days =  models.CharField(max_length=200)
    note = models.CharField(max_length=1500,blank=True, null=True)
    class Meta:
        verbose_name = 'contact meta property'
        verbose_name_plural = 'contact meta properties'

class ProfileMetaProp(models.Model):
    title = models.CharField(max_length=150,blank=True, null=True)
    email = models.EmailField()
    from_email = models.EmailField()
    smtp_server =  models.CharField(max_length=150) 
    smtp_port =  models.CharField(max_length=10)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200) 
    moto  = models.CharField(max_length=250,blank=True, null=True)
    message = models.CharField(max_length=2500,blank=True, null=True)
    class Meta:
        verbose_name = 'profile meta property'
        verbose_name_plural = 'profile meta properties'
 

class MetaProp(models.Model):
    title = models.CharField(max_length=140)
    keywords = models.CharField(max_length=1600)
    description  =  models.TextField(max_length=1500)
    author  =  models.CharField(max_length=140)
    analytics =  models.CharField(max_length=60)
    # meta class
    class Meta:
        verbose_name = 'meta property'
        verbose_name_plural = 'meta properties'


class MetaPropAdmin(admin.ModelAdmin):
    fields = ('title','keywords','description','author','analytics')

class ContactMetaPropAdmin(admin.ModelAdmin):
    fields = ('title','address1','address2','city','zip','state','phone','fax','hours','days','note')

class ProfileMetaPropAdmin(admin.ModelAdmin):
    fields = ('title','email','from_email','smtp_server','smtp_port','user_name','password','moto','message')
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ProfileMetaPropAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'message':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


admin.site.register(MetaProp)
admin.site.register(ContactMetaProp)
admin.site.register(ProfileMetaProp)
