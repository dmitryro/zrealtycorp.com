from __future__ import print_function
from periodically.decorators import *
from periodically import register
from datetime import timedelta
import django_filters
import smtplib
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from restless.views import Endpoint
from metaprop.models import ProfileMetaProp
from periodically.decorators import *


@every(minutes=1)
def task2():
    print('RUNNING exampleapp.periodictasks.task2')
    raise Exception('Custom exception!')


def task3():
    print('RUNNING exampleapp.periodictasks.task3')
register.simple_task(task3, Every(timedelta(weeks=2)))


@daily(hour=19, minute=38)
@daily(hour=19, minute=38) # Duplicate. Shouldn't reschedule.
@daily(hour=20, minute=13) # Not a duplicate. Should schedule again.
def task4():
    print('RUNNING exampleapp.periodictasks.task4')

@every(minutes=2)
def send_email_task():
        id = 1
        name = 'ZRealty System'
        email = 'dmitryro@gmail.com'
        phone = '718 404 6471'
        title = 'System health check'
        mess = 'We are still up and running'


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

