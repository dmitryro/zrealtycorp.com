from django.http import HttpResponseRedirect
from django.conf import settings
from django.db import connection
from django.shortcuts import render
from time import time
from operator import add
from re import compile
import re

 
EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]
 
class LoginMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated():
             return render(request,"dashboard.html",{}) 
        else:
             return render(request,"/login/google-oauth2/complete",{})

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass


