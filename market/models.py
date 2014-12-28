from django.db import models

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=150)
    date_start = models.DateTimeField("Active since")
    date_ends = models.DateTimeField("Active until")

   
class Social(models.Model):
    pass 
