"""
 Property models
 Author: Dmitry Roitman
 2014
"""
import binascii
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from phonenumber_field.modelfields import PhoneNumberField


class Token(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super(Token, self).save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __unicode__(self):
        return self.token

"""
  Property implementation
"""
@python_2_unicode_compatible
class Subscription(models.Model):
    name = models.CharField(max_length=200)
      
    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('pl-subscription', args=[self.slug])

"""
  Member Roles
"""
@python_2_unicode_compatible
class MemberRole(models.Model):

    name = models.CharField(max_length=100) 

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = 'member role'
        verbose_name_plural = 'Member Roles'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pl-member-roles', args=[self.slug])


"""
  Member login
"""
@python_2_unicode_compatible
class Login(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'login'
        verbose_name_plural = 'logins'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('pl-logins', args=[self.slug])


"""
  Property implementation
"""
@python_2_unicode_compatible
class Member(models.Model):
    who_are_you = models.ForeignKey(MemberRole, blank=True, null=True)
    subscription = models.ForeignKey(Subscription,blank=True, null=True)
    confirm_password = models.CharField(max_length=40)
    username = models.CharField(max_length=40,blank=True, null=True)
    password = models.CharField(max_length=40,blank=True, null=True)
    email = models.EmailField(max_length=140,blank=True, null=True)
    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('pl-members', args=[self.slug])

    def set_username(self,user):
        self.username = user

    def set_password(self, password):
        self.password = password

    def set_first(self, first):
        self.first = first

    def set_last(self, last):
        self.last = last

    def set_phone(self,phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_who_are_you(self, who):
        self.who_are_you = who


class MemberAdmin(admin.ModelAdmin):
    fields = ('first','last','email','username','password','confirm_password','who_are_you','subscribe_to','webpage','twitter','linkedin','facebook','google','about')


class MemberRoleAdmin(admin.ModelAdmin):
    fields = ('name')

class SubscriptionAdmin(admin.ModelAdmin):
    fields = ('name')


admin.site.register(Subscription)
admin.site.register(MemberRole)
admin.site.register(Member)
