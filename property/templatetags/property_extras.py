import logging
import re
import sys
from urlparse import urlparse
from django.template import Library, Node, NodeList, TemplateSyntaxError
from django.utils.encoding import smart_str
from property.models import Property
from property.forms import SearchForm 
from tagging.models import Tag, TaggedItem
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

kw_pat = re.compile(r'^(?P<key>[\w]+)=(?P<value>.+)$')
logger = logging.getLogger('sorl.thumbnail')

@register.simple_tag
def property_category(category, *args, **kwargs):
    pass


@register.simple_tag
def property_image_one(a, *args, **kwargs):
    path = str(a)
    id = path[10:len(path)]
    property = Property.objects.get(property_id=id)
    return property.picture1

@register.simple_tag
def property_search(*args, **kwargs):
    pass 

@register.simple_tag
def property_similar(br,nb,rms,*args, **kwargs):
     properties = Property.objects.get(borough=br,neighborhood=nb,rooms=rm)
     return properties

	
@register.simple_tag
def property_meta(a, b, *args, **kwargs):

    path = str(a)
    id = path[10:len(path)]
    property = Property.objects.get(property_id=id)

    if (b==1):
        return property.picture1
    elif (b==2):
        return property.picture2
    elif (b==3):
        return property.picture3
    elif (b==4):
        return property.picture4
    elif (b==5):
        return property.title
    elif (b==6):
        return property.type
    elif (b==7):
        return property.category
    elif (b==8):
        return property.borough
    elif (b==9):
        return property.neighborhood
    elif (b==10):
        return property.description
    elif (b==11):
        return property.rooms
    elif (b==12):
        return property.bathrooms
    elif (b==13):
	if property.pets_allowed:
            return 'Yes'
        return 'No'
    elif (b==14):
        return property.price
    elif (b==15):
        return property.published
    elif (b==16):
        return property.property_id


    

 
