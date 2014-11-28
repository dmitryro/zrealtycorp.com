"""
Django settings for zrealty project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
try:
    from local_settings import *
except ImportError:
    from default_settings import *

