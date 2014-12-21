"""
Created on Jul 6, 2014
@author: Dmitry Roitman
"""
import django_filters
import smtplib
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework import viewsets
from registration_api import utils
from restless.views import Endpoint
from property.serializers import PropertySerializer
from property.serializers import CategorySerializer
from property.serializers import StatusSerializer
from property.serializers import TypeSerializer
from property.serializers import NeighborhoodSerializer
from property.serializers import BoroughSerializer
from property.serializers import RoomsSerializer
from property.models import Property, Room, Category, Type, Status, Neighborhood, Borough
from property.views import JSONResponse
from metaprop.models import ProfileMetaProp
from models import UserProfile
from utils.models import Member

register = template.Library()

class SearchViewMixin(object):
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


class SearchView(SearchViewMixin, Endpoint):
    def get(self, request):
        rooms = request.params.get('rooms_id','')
        type = request.params.get('type_id','')       
        category = request.params.get('category_id','')
        borough = request.params.get('borough_id','')
        neighborhood = request.params.get('neighborhood_id','')
        pets_allowed = request.params.get('pets_allowed','')
        min_price = request.params.get('min_price','')
        max_price = request.params.get('max_price','')

        try:
            properties = Property.objects.filter(category_id=category, rooms_id=rooms, 
                                                 type_id=type, borough_id=borough, 
                                                 neighborhood_id=neighborhood, 
                                                 pets_allowed=pets_allowed)
        except Exception,R:
            print R

        serializer = PropertySerializer(properties, many=True)
        return JSONResponse(serializer.data)


    def post(self, request):
        name = 'test'
        return {'message': 'Hello, %s!' % name}  


class EmailView(Endpoint):

    def containsnonasciicharacters(str):
        return not all(ord(c) < 128 for c in str)   

    def addheader(message, headername, headervalue):
        if containsnonasciicharacters(headervalue):
            h = Header(headervalue, 'utf-8')
            message[headername] = h
        else:
            message[headername] = headervalue    
        return message

    def get(self, request):
        id = request.params.get('id','')
        name = request.params.get('name','')
        email = request.params.get('email','') 
        phone = request.params.get('phone','')
        title = request.params.get('title','')
        mess = request.params.get('message','')

 
        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = profile.email
        TO = profile.email
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server
      
 
        BODY='<html><body><strong>ID</strong> %s'%id
        BODY+='</strong><br/><strong>TITLE</strong> %s'%title
        BODY+='</strong><br/><strong>NAME</strong> %s'%name
        BODY+='</strong><br/><strong>EMAIL</strong> %s'%email
        BODY+='</strong><br/><strong>PHONE</strong> %s'%phone 
        BODY+='</strong><br/><strong>MESSAGE</strong> %s'%mess 
        BODY+='</strong></body></html>'

        SUBJECT = 'ZRealtyCorp Inquiry %s'%id
        message = 'Subject: %s\n\n%s' % (SUBJECT, BODY)


        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
            Your mail reader does not support the report format.
            Please visit us <a href="http://www.mysite.com">online</a>!"""
 
        HTML_BODY  = MIMEText(BODY.encode('utf-8'), 'html','utf-8')

 
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
        MESSAGE.attach(HTML_BODY)

        msg = MESSAGE.as_string()
      
        server = smtplib.SMTP(SERVER+':'+PORT)
        server.ehlo()
        server.starttls()
        server.login(USER,PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()

        return {'message': 'Hello, %s!' % name}

"""
  Contact View - processing the general contact form
"""
class ContactView(EmailView):

    def get(self, request):
        subject = request.params.get('subject','')
        name = request.params.get('name','')
        email = request.params.get('email','')
        mess = request.params.get('message','')

        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = profile.email
        TO = profile.email
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server

        BODY='<html><body><strong>NAME</strong> %s'%name
        BODY+='</strong><br/><strong>SUBJECT</strong> %s'%subject
        BODY+='</strong><br/><strong>EMAIL</strong> %s'%email
        BODY+='</strong><br/><strong>MESSAGE</strong> %s'%mess
        BODY+='</strong></body></html>'

        SUBJECT = 'General Inquiry from %s'%name
        message = 'Subject: %s\n\n%s' % (SUBJECT, BODY)


        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
            Your mail reader does not support the report format.
            Please visit us <a href="http://www.mysite.com">online</a>!"""

        HTML_BODY  = MIMEText(BODY.encode('utf-8'), 'html','utf-8')


    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
        MESSAGE.attach(HTML_BODY)
        msg = MESSAGE.as_string() 
        server = smtplib.SMTP(SERVER+':'+PORT)
        server.ehlo()
        server.starttls()
        server.login(USER,PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()


        return {'message': 'Hello, %s!' % name}



"""
  Activate View - processing the activation email notification
"""
class ActivateView(EmailView):

    def get(self, request):
        # Populate the user credentials
        username = request.params.get('username','')
        password = request.params.get('password','')
        email = request.params.get('email','')
        mess = 'Welcome to ZRealty.'
        
        user = User.objects.get(username=username)  
        activation = utils.create_activation_key(user)
        link = 'http://zrealtycorp.com/accounts/activate/%s'%activation

        try:
            member = UserProfile(user_id=user.id, activation_key=activation)
            member.save()
        except:
            pass
           # new_profile.save()

        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = profile.email
        TO = profile.email
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server

        #contstruct the message
        BODY='<html><body><strong>USERNAME</strong> %s'%username
        BODY+='</strong><br/><strong>PASSWORD</strong> %s'%password
        BODY+='</strong><br/><strong>EMAIL</strong> %s'%email
        BODY+='</strong><br/><strong>MESSAGE</strong> %s'%mess
        BODY+='</strong><br/><strong>PLEASE FOLLOW THE LINK: </strong> '
        BODY+='<a href="%s">activate</a>'%link
        BODY+='</strong></body></html>'

        SUBJECT = 'New account notification for %s'%username
        message = 'Subject: %s\n\n%s' % (SUBJECT, BODY)


        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
            Your mail reader does not support the report format.
            Please visit us <a href="http://www.mysite.com">online</a>!"""

        HTML_BODY  = MIMEText(BODY.encode('utf-8'), 'html','utf-8')


    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
        MESSAGE.attach(HTML_BODY)
        msg = MESSAGE.as_string()
        server = smtplib.SMTP(SERVER+':'+PORT)
        server.ehlo()
        server.starttls()
        server.login(USER,PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()


        return {'message': 'Hello, %s!' % name}


"""
  Notify View - processing the general contact form
"""
class NotifyView(EmailView):

    def get(self, request):
        # Populate the user credentials
        username = request.params.get('username','')
        password = request.params.get('password','')
        email = request.params.get('email','')
        mess = 'A new account has been created for you. We will activate it shortly'
 
        # Set the general SMTP server 
        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = profile.email
        TO = profile.email
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server

        #contstruct the message
        BODY='<html><body><strong>USERNAME</strong> %s'%username
        BODY+='</strong><br/><strong>PASSWORD</strong> %s'%password
        BODY+='</strong><br/><strong>EMAIL</strong> %s'%email
        BODY+='</strong><br/><strong>MESSAGE</strong> %s'%mess
        BODY+='</strong></body></html>'

        SUBJECT = 'New account notification for %s'%username
        message = 'Subject: %s\n\n%s' % (SUBJECT, BODY)


        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
            Your mail reader does not support the report format.
            Please visit us <a href="http://www.mysite.com">online</a>!"""

        HTML_BODY  = MIMEText(BODY.encode('utf-8'), 'html','utf-8')


    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
        MESSAGE.attach(HTML_BODY)
        msg = MESSAGE.as_string()
        server = smtplib.SMTP(SERVER+':'+PORT)
        server.ehlo()
        server.starttls()
        server.login(USER,PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()


        return {'message': 'Hello, %s!' % name}


"""
Category ViewSet
"""
class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows properties to be viewed or edited.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer



"""
Category ViewSet
"""
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



"""
Rooms ViewSet
"""
class RoomsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomsSerializer


"""
Type ViewSet
"""
class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows types to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

"""
Status ViewSet
"""
class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows statuses to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


"""
Neighborhood ViewSet
"""
class NeighborhoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows neighborhoods to be viewed or edited.
    """
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

"""
Borough ViewSet
"""
class BoroughViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows boroughs to be viewed or edited.
    """
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer

"""
Property of a type ViewSet
"""
class PropertyTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows property with a type to be viewed or edited.
    """
  
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = Property.objects.all()
        propertytype = self.request.QUERY_PARAMS.get('type',None)
        if propertytype is not None:
            queryset = queryset.filter(type=propertytype)
        return queryset

"""
Activate
"""
def register_activate(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/home')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    user = User.objects.get(id=user_profile.user_id)
    user.is_active = True
    user.save()
    return render_to_response('activated.html')

      


