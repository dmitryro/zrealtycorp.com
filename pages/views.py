from django.contrib import messages
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.context import RequestContext
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.core.mail import send_mail
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from smtplib import SMTP
import email.Charset
import html2text 
from feedparser import _sanitizeHTML
from django.conf import settings
from BeautifulSoup import BeautifulSoup
from zrealty import settings
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
import rules_light
from braces import views
from braces.views import AnonymousRequiredMixin
from property.models import Property
from agent.models import Agent
from property.forms import SearchForm
from forms import ContactForm
from forms import ContactModelForm
from models import MaintenancePage


"""
Property Details View Mixin - set the context data
"""

class PropertyDetailViewMixin(object):
    def get_context_data(self,**kwargs):
        url = self.request.get_full_path()
        path = str(url)
        id = path[10:len(path)]
        property = Property.objects.get(property_id=id)
        related = Property.objects.filter(borough=property.borough,neighborhood=property.neighborhood,category=property.category)

        context = super(PropertyDetailViewMixin,
                  self).get_context_data(**kwargs)
        form =  SearchForm()
        context['property_form'] = form
        context['property_id'] = len(related)
        context['related'] = related

        return context

"""
Maintenance View Mixin - set the context data
"""
class MaintenanceViewMixin(object):
    def get_context_data(self,**kwargs):
        maintenance = MaintenancePage.objects.filter(id=1)
        context = super(MaintenanceViewMixin,self).get_context_data(**kwargs)
        try:
            context['contact'] = maintenance.contact
        except:
            pass

class HomeViewMixin(object):
    def get_context_data(self,**kwargs):
        properties = Property.objects.all()
        context = super(HomeViewMixin,
                  self).get_context_data(**kwargs)
        avatars = []

        for property in properties:
           avatars.append(property.picture1)

        page_size = settings.PAGING_PAGE_SIZE
        context["results_per_page"] = page_size
        context['front_properties'] = properties
        context['is_paginated'] = True
        form =  SearchForm()
        context['property_form'] = form
        return context


"""
Featured View Mixing - set the context data
"""
class FeaturedViewMixin(object):
    def get_context_data(self,**kwargs):
        properties = Property.objects.filter(is_featured=True)
        context = super(FeaturedViewMixin,
                  self).get_context_data(**kwargs)
        avatars = []

        for property in properties:
           avatars.append(property.picture1)

        page_size = settings.PAGING_PAGE_SIZE
        context["results_per_page"] = page_size
        context['featured_properties'] = properties
        context['is_paginated'] = True
        form =  SearchForm()
        context['property_form'] = form

    #    form =  SearchForm()
    #    context['property_form'] = form

        return context




"""
Rent View Mixin - set the context data
"""
class RentViewMixin(object):
    def get_context_data(self,**kwargs):
        properties = Property.objects.filter(category_id=1)
        context = super(RentViewMixin,
                  self).get_context_data(**kwargs)
        avatars = []

        for property in properties:
           avatars.append(property.picture1)

        page_size = settings.PAGING_PAGE_SIZE
        context["results_per_page"] = page_size
        context['rent_properties'] = properties
        context['is_paginated'] = True
        form =  SearchForm()
        context['property_form'] = form

    #    form =  SearchForm()
    #    context['property_form'] = form
  
        return context
"""
Sale View Mixin - set the context data
"""
class SalesViewMixin(object):
    def get_context_data(self,**kwargs):
        properties = Property.objects.filter(category_id=2)
        context = super(SalesViewMixin,
                  self).get_context_data(**kwargs)
        avatars = []

        for property in properties:
           avatars.append(property.picture1)

        page_size = settings.PAGING_PAGE_SIZE
        context["results_per_page"] = page_size
        context['sales_properties'] = properties
        context['is_paginated'] = True
        form =  SearchForm()
        context['property_form'] = form

  #      form =  SearchForm()
   #     context['property_form'] = form
 
        return context



"""
Agent View Mixin - set the context data
"""
class AgentViewMixin(object):
    def get_context_data(self,**kwargs):
        agents = Agent.objects.all()
        context = super(AgentViewMixin,
                  self).get_context_data(**kwargs)

        page_size = settings.PAGING_PAGE_SIZE
        context["results_per_page"] = page_size
        context['agents'] = agents
        context['is_paginated'] = True
        form =  SearchForm()
        context['property_form'] = form

        return context



"""
  Blog View Mixin
"""
class BlogViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(BlogViewMixin,
                  self).get_context_data(**kwargs)
        form =  SearchForm()
        context['property_form'] = form

        return context


"""
  About View Mixin
"""
class AboutViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(AboutViewMixin,
                  self).get_context_data(**kwargs)
        form =  SearchForm()
        context['property_form'] = form

        return context



"""
Contact View Mixin
"""
class ContactViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(ContactViewMixin,
                  self).get_context_data(**kwargs)
        contactform = ContactForm()   
        form =  SearchForm()
        context['property_form'] = form
        context['form'] = contactform
        context['layout'] = 'vertical'
	return context


"""
RSS View Mixin
"""

class RssViewMixin(object):
    def get_context_data(self,**kwargs):
        feeds = Feed.objects.all()
        context = super(ContactViewMixin,
                  self).get_context_data(**kwargs)
  
        context['entries'] = feeds
        return context


"""
Search View Mixin 
"""
class SearchViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(SearchViewMixin,
                  self).get_context_data(**kwargs)
      #  form =  SearchForm()
      #  context['property_form'] = form
 
        return context

class MobileViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(MobileViewMixin,
                  self).get_context_data(**kwargs)
      #  form =  SearchForm()
      #  context['property_form'] = form

        return context



class MaintenanceView(MaintenanceViewMixin,TemplateView):
            template_name = "maintenance.html"

class HomeView(HomeViewMixin, TemplateView):
            template_name = "home.html"

class MobileView(MobileViewMixin, TemplateView):
            template_name = "mobile.html"

class RentView(RentViewMixin, TemplateView):
            template_name = "rentals.html"

class FeaturedView(FeaturedViewMixin, TemplateView):
            template_name = "featured.html"


class SalesView(SalesViewMixin, TemplateView):
            template_name = "sales.html"


class AboutView(AboutViewMixin,TemplateView):
	    template_name = "about.html"

class AgentView(AgentViewMixin,TemplateView):
            template_name = "agents.html"

class RssView(RssViewMixin, TemplateView):
            template_name = "rss.html"

class BlogView(BlogViewMixin, TemplateView):
            template_name = "blog.html"

class PropertyDetailView(PropertyDetailViewMixin, TemplateView):
    template_name = "details.html"


class SearchFormView(SearchViewMixin,TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchFormView, self).get_context_data(**kwargs)
        context.update(property_form=SearchForm())
        return context

"""
Custom dashboard page view
"""

class DashboadView(AnonymousRequiredMixin, TemplateView):
    authenticated_redirect_url = u"/dashboard/"

"""
Contact page view
"""
class ContactView(ContactViewMixin,TemplateView):
    template_name = 'contact.html'


def contact_form_with_template(request):

    layout = request.GET.get('layout')
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.is_valid()
        if(form.is_valid()):
            messages.success(request, 'Your message hass been successfully sent.')
            sendmail('dmitryro@gmail.com','Subject here', 'Here is the message.', attach=[], mtype='html')
            send_html_mail('subject',"no-reply@example.com","dmitryro@gmail.com", context=None,
                            html_template="", text_template="", sender_name="Dmitry",
                            html_content="", text_content="", recip_list=None, sender_formatted="")
    else:
        form = ContactForm()
        modelform = ContactModelForm()
    return render_to_response('contact.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))


def contact_form(request):
    return render_to_response('contact.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))
