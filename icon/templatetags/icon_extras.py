import logging
import re
import sys
from urlparse import urlparse
from django.template import Library, Node, NodeList, TemplateSyntaxError
from django.utils.encoding import smart_str
from icon.models import Icon, SocialIcon
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
 Get the icon meta
"""
@register.simple_tag
def icon_meta(a, b, *args, **kwargs):

    try:
        icon = Icon.objects.get(id=int(a))
        if (b==1):
            return icon.title
        elif (b==2):
            return icon.url
        elif (b==3):
            return icon.icon_thumbnail.url
        elif (b==4):
            return icon.icon_thumbnail.height
        elif (b==5):
            return icon.icon_thumbnail.width

    except TypeError:
        print "Invalid argument type"

    except NameError:
        print "No result for this id"

    except icon.DoesNotExist: 
        print "Could not find any icons matching the parameter"


"""
 Get the icon meta
"""
@register.simple_tag
def social_icon_meta(a, b, *args, **kwargs):

    try:
        icon = SocialIcon.objects.get(id=int(a))
        if (b==1):
	    return icon.title
	elif (b==2):
	    return icon.url
	elif (b==3):
	    return icon.icon_thumbnail.url
	elif (b==4):
            return icon.icon_thumbnail.height
	elif (b==5):
	    return icon.icon_thumbnail.width

    except TypeError:
	print "Invalid argument type"

    except NameError:
	print "No result for this id"

    except icon.DoesNotExist:
	print "Could not find any icons matching the parameter"



