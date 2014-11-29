import logging
import re
import sys
from urlparse import urlparse
from django.template import Library, Node, NodeList, TemplateSyntaxError
from django.utils.encoding import smart_str
from icon.models import ActionIcon
from tagging.models import Tag, TaggedItem
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

kw_pat = re.compile(r'^(?P<key>[\w]+)=(?P<value>.+)$')
logger = logging.getLogger('sorl.thumbnail')

@register.simple_tag
def dashboard_meta(a, b, *args, **kwargs):

    action = ActionIcon.objects.get(action_id=a)

    if (b==1):
        return action.title
    elif (b==2):
        return action.icon
    elif (b==3):
        return a
    elif (b==4):
        return action.width
    elif (b==5):
        return action.height

