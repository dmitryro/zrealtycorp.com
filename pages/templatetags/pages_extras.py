from django import template
from pages.forms import ContactForm
from property.forms import SearchForm
register = template.Library()

@register.inclusion_tag('cform.html')
def contact_form():
    return {'contact_form': ContactForm()}



#@register.inclusion_tag('search.html')
#def inquiry_form():
 #   return {'inquiry_form': SearchForm()}


