import logging
import re
import sys
from urlparse import urlparse
from django.template import Library, Node, NodeList, TemplateSyntaxError
from django.utils.encoding import smart_str
from logo.models import Logo
from tagging.models import Tag, TaggedItem
from django import template
from django.template.defaultfilters import stringfilter
from PIL import Image,ImageEnhance
import urllib2 as urllib			
from cStringIO import StringIO
from zrealty.settings import MEDIA_URL

register = template.Library()

kw_pat = re.compile(r'^(?P<key>[\w]+)=(?P<value>.+)$')
logger = logging.getLogger('sorl.thumbnail')

"""
 Get the logo meta
"""
@register.simple_tag
def logo_meta(a, b, *args, **kwargs):

    try:
        logo = Logo.objects.get(id=int(a))
        if (b==1):
            return logo.title
        elif (b==2):
            return logo.version
        elif (b==3):
            return logo.logo_thumbnail.url
        elif (b==4):
            return logo.logo_thumbnail.height
        elif (b==5):
            return logo.logo_thumbnail.width
        elif (b==6):
            return logo.slogan
 
    except TypeError:
        print "Invalid argument type"

    except NameError:
        print "No result for this id"

 
