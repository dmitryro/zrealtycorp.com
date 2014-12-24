from django.db import connection
from time import time
from operator import add
import re


class LoginMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass


