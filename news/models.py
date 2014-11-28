from django.db import models
from django.contrib import admin
# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField(max_length=300)
    expiration = models.DateTimeField('Expiration Date');
    
class MessageAdmin(admin.ModelAdmin):
    fields = ('title','message','expiration')

admin.site.register(Message)


