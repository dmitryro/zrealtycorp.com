"""
Django settings for zrealty project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+7&2ugf)%qqn_nh29443z$au)or1z_o$h@sk34w_b34uf)24k$'
SITE_ID = 1
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Social Authentication Settings
FACEBOOK_APP_ID              = '818921438134206'
FACEBOOK_API_SECRET          = '2882cb362e766e24a1a51be251860a26'
TWITTER_CONSUMER_KEY = 'juXvnN6hyNhEK7refjdQ'
TWITTER_CONSUMER_SECRET = 'A1PEleM5SMFDtR57AJUFdPB2iKjEH4ROgSoeQiY5Aeo' 
TWITTER_API_ACCESS_TOKEN_CALLBACK = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'AIzaSyCDUnYCyzEf8M6S1wyFvyeacZF9vO37l70'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '-vOyys9JyMeTG53QgA18dWcY'
SOCIAL_AUTH_GOOGLE_OAUTH2_CLIENT_ID      = '416241165113-d3567f5kdtb1fivlse2aivg8gvb8llh6.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_CLIENT_SECRET  = '-vOyys9JyMeTG53QgA18dWcY'
SOCIAL_AUTH_GOOGLE_OAUTH2_CLIENT_EMAIL_ADDRESS = '416241165113-d3567f5kdtb1fivlse2aivg8gvb8llh6@developer.gserviceaccount.com'
SOCIAL_AUTH_TWITTER_KEY = 'juXvnN6hyNhEK7refjdQ'
SOCIAL_AUTH_TWITTER_SECRET = 'A1PEleM5SMFDtR57AJUFdPB2iKjEH4ROgSoeQiY5Aeo'
SOCIAL_AUTH_FACEBOOK_SECRET='2882cb362e766e24a1a51be251860a26'
SOCIAL_AUTH_FACEBOOK_KEY = '818921438134206'
SOCIAL_AUTH_FACEBOOK_ID = '818921438134206'
SOCIAL_AUTH_FACEBOOK_EXTENDED_PERMISSIONS = ['email']
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
SOCIAL_AUTH_SESSION_EXPIRATION = False
SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook','twitter','google','github')
SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'
SOCIAL_AUTH_DEFAULT_USERNAME = lambda u: slugify(u) # you'll need to import slugify from 'django.template.defaultfilters'
SOCIAL_AUTH_EXTRA_DATA = False
SOCIAL_AUTH_CHANGE_SIGNAL_ONLY = True
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UID_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16

# Application definition

# Possible values are Tokenizer (default), JaroWinkler and LevenshteinDistance.
# JaroWinkler and LevenshteinDistance require Levenshtein Module >= 0.10.1.
USER_AGENT_SEARCH_ALGORITHM = 'Tokenizer'

FEEDBURNER_URLS = {
    '/feeds/latest/': 'http://feeds.feedburner.com/ZrealtyCorpSiteNews',
}

EASY_MAPS_CENTER = (-41.3, 32)

#SOUTH_MIGRATION_MODULES = {
#    'easy_thumbnails': 'easy_thumbnails.south_migrations',
#    'taggit': 'taggit.south_migrations',
#}

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
#    'django.contrib.comments',
    'django.contrib.syndication',
    #contributed apps

   # 'modernizr',
    'admin_tools',
    'adminsortable',
  #  'ajax_select',
    'allauth',
    'allauth.account',
    'any_urlfield',
    'autocomplete_light',
  #  'bbfreeze',
    'bootstrap',
    'bootstrap_toolkit', 
    'bootstrap_pagination',
    'braces',
    'corsheaders',
    'coffeescript',
    'debug_toolbar',
    'django_actions',
    'django_extensions',
    'django_facebook',
    'django_feedburner',
    'django_filters',
    'django_google_maps',
    'django_mobile',
    'django_rules',
    'django_select2',
    'djangosecure',
    'django_rq',
    'djangular',
    'djcelery',
    'geopy', 
    'django_seo_js', 
    'easy_maps',
    'easy_thumbnails',
    'endless_pagination',
    'facebook',
    'fancy_autocomplete',
   # 'feedme',
   # 'feedreader',
    'feedjack',
    'funcy',
    'geoposition',
    'gmapi',
    'i18n',
    'image_cropping',
    'imagekit',
    'jquery',
    'jquery_lightbox',
    'kombu.transport.django', 
    'less',
    'logical_rules',
    'missing',
    'microblogging',
    'navigation',
    'notifications', 
    'oauth_access',
    'pagination',
    'permission',
    'pipeline',
    'phonenumber_field',
    'provider',
    'provider.oauth2',
    'pygments',
    'redis',
    'registration_api',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_framework_digestauth',
    'restless',
    'rules_light',
    'selectable',
    'selenium',
    'socialauth',
    'social',
    'twitter',
    'twitter_api',
    'taxonomy',
    'tastypie',
    'tooltips', 
    'smart_selects',
    'social_auth',
    'socialregistration',
    'voting',
    'uni_form',
    # Custom apps
    'agent',
    'dashboard',
    'icon',
    'feeds',
    'logo',
    'metaprop',
    'pages',
    'property',
    'utils',
    'api',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'pagination_bootstrap.middleware.PaginationMiddleware',
    'django_seo_js.middleware.UserAgentMiddleware',  
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'rules_light.middleware.Middleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = {
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django_facebook.context_processors.facebook",
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_login_redirect',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
}

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.orkut.OrkutBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.contrib.readability.ReadabilityBackend',
    'social_auth.backends.contrib.fedora.FedoraBackend',

    'django.contrib.auth.backends.ModelBackend',
    'django_rules.backends.ObjectPermissionBackend',
)
   
LOGIN_REDIRECT_URL = '/dashboard/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard'
SOCIAL_AUTH_ERROR_KEY='social_errors'
SOCIAL_AUTH_EXPIRATION = 'expires'
#SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'            
SOCIAL_AUTH_RAISE_EXCEPTIONS = DEBUG
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_SESSION_EXPIRATION = False

# 'magic' settings
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'en_US'}

#AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
#AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'
GITHUB_API_KEY = ''
GITHUB_API_SECRET = ''
GOOGLE_CONSUMER_KEY          = 'AIzaSyCDUnYCyzEf8M6S1wyFvyeacZF9vO37l70'
GOOGLE_CONSUMER_SECRET       = '-vOyys9JyMeTG53QgA18dWcY'
GOOGLE_OAUTH2_CLIENT_ID      = '416241165113-d3567f5kdtb1fivlse2aivg8gvb8llh6.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = '-vOyys9JyMeTG53QgA18dWcY'
GOOGLE_OAUTH2_CLEINT_EMAIL   = '416241165113-rl80a3mehm6ghoq8j9g0lqpvukuqq1qr@developer.gserviceaccount.com'
GOOGLE_WHITE_LISTED_DOMAINS = ['zrealtycorp.com']
GOOGLE_WHITE_LISTED_EMAILS= ['dmitryro@gmail.com','416241165113-d3567f5kdtb1fivlse2aivg8gvb8llh6@developer.gserviceaccount.com']
# 'magic' settings
SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'


SOCIAL_AUTH_ENABLED_BACKENDS = ('google', 'google-oauth', 'facebook','twitter','github','linkedin')
"""
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',

    'core.utils.associate_by_email',

    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)
SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    'social.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social.pipeline.disconnect.disconnect'
)
"""
ROOT_URLCONF = 'zrealty.urls'

WSGI_APPLICATION = 'zrealty.wsgi.application'

# The name of a build profile to use for your project, relative to REQUIRE_BASE_URL.
# A sensible value would be 'app.build.js'. Leave blank to use the built-in default build profile.
# Set to False to disable running the default profile (e.g. if only using it to build Standalone
# Modules)
REQUIRE_BUILD_PROFILE = None

# The name of the require.js script used by your project, relative to REQUIRE_BASE_URL.

# A dictionary of standalone modules to build with almond.js.
# See the section on Standalone Modules, below.
REQUIRE_STANDALONE_MODULES = {}

# Whether to run django-require in debug mode.

# A tuple of files to exclude from the compilation result of r.js.
REQUIRE_EXCLUDE = ("build.txt",)

# The execution environment in which to run r.js: auto, node or rhino.
# auto will autodetect the environment and make use of node if available and rhino if not.
# It can also be a path to a custom class that subclasses require.environments.Environment and defines some "args" function that returns a list with the command arguments to execute.
REQUIRE_ENVIRONMENT = "auto"
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zrealty',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
   }
}

DEFAULT_AUTHENTICATION = (
   # 'rest_framework.authentication.BasicAuthentication',
   # 'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.OAuth2Authentication',
)

GRAPPELLI_ADMIN_TITLE = 'ZRealty Corp'

GRAPPELLI_INDEX_DASHBOARD = {
   'django.contrib.admin.site': 'artwell.dashboard.CustomIndexDashboard',
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.SessionAuthentication',
       'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.OAuth2Authentication',
     ),
    'DEFAULT_PARSER_CLASSES': (

        'rest_framework.parsers.YAMLParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'PAGINATE_BY': 1000, 

    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',
 
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/vhosts/zrealtycorp.com/zrealty/static/'
MEDIA_ROOT = '/var/www/vhosts/zrealtycorp.com/zrealty/media/'
MEDIA_URL = '/media/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "rq_console": {
            "format": "%(asctime)s %(message)s",
            "datefmt": "%H:%M:%S",
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        "rq_console": {
            "level": "DEBUG",
            "class": "rq.utils.ColorizingStreamHandler",
            "formatter": "rq_console",
            "exclude": ["%(asctime)s"],
        },
        # If you use sentry for logging
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        "rq.worker": {
            "handlers": ["rq_console"],
            "level": "DEBUG"
        },
    }
}




CACHES = {
    "default": {
    "BACKEND": "redis_cache.cache.RedisCache",
    "LOCATION": "127.0.0.1:6379:1",
    "OPTIONS": {
                "CLIENT_CLASS": "redis_cache.client.DefaultClient",
                'DB' : 1,
                #'PASSWORD': 'yadayada',
                'PARSER_CLASS': 'redis.connection.HiredisParser'
               }
    },
    'resources': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'TIMEOUT': 60
    }
}

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': 'some-password',
        'DEFAULT_TIMEOUT': 360,
    },
    'high': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379'), # If you're on Heroku
        'DB': 0,
        'DEFAULT_TIMEOUT': 500,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    }
}

SITE_DOMAIN = 'zrealtycorp.com'

SITE_NAME = 'zrealtycorp'

STATICFILES_DIRS = (
  './static_files',
  './static_files/css',
  './static_files/css/themes',
  './static_files/js',
  './static_files/js',
  './static_files/js/angular',
  './static_files/js/require',
  './static_files/js/jquery',
  '/usr/local/lib/python2.7/site-packages/grappelli/static',
#  '/usr/local/lib/python2.7/site-packages/rest_framework/static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'coffeescript.finders.CoffeescriptFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

COMPRESS_OFFLINE = True
# See the django-compressor docs at http://django_compressor.readthedocs.org/en/latest/settings/
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
)


TEMPLATE_LOADERS = (
     ('django_mobile.loader.CachedLoader', (
            'django_mobile.loader.Loader',
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
     )),
     ('pyjade.ext.django.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader',
     )),

     ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
TEMPLATE_DIRS = (
    '/var/www/vhosts/zrealtycorp.com/zrealty/templates/',
    '/var/www/vhosts/zrealtycorp.com/zrealty/api/templates/',   
    '/var/www/vhosts/zrealtycorp.com/zrealty/pages/templates/',
    '/usr/local/lib/python2.7/site-packages/pinax_theme_bootstrap/templates',
    '/usr/local/lib/python2.7/site-packages/djfrontend/templates',
    '/usr/local/lib/python2.7/site-packages/sekizai/test_templates',
    '/usr/local/lib/python2.7/site-packages/bootstrap_toolkit/templates',
    '/var/www/vhosts/zrealtycorp.com/zrealty/Django-Socialauth/build/lib/socialauth/templates',
    '/usr/local/lib/python2.7/site-packages/grappelli/templates',
)
CORS_ORIGIN_ALLOW_ALL = True
# Backend to use
SEO_JS_BACKEND = "django_seo_js.backends.PrerenderIO"   # Default

# Whether to run the middlewares and update_cache_for_url.  Useful to set False for unit testing.
SEO_JS_ENABLED = True # Defaults to *not* DEBUG.

# User-agents to render for, if you're using the UserAgentMiddleware
# Defaults to the most popular.  If you have custom needs, pull from the full list:
# http://www.useragentstring.com/pages/Crawlerlist/
SEO_JS_USER_AGENTS = [
    "Googlebot",
    "Yahoo",
    "bingbot",
    "Badiu",
    "Ask Jeeves",
]

# Urls to skip the rendering backend, and always render in-app.
# Defaults to excluding sitemap.xml.
SEO_JS_IGNORE_URLS = [
    "/sitemap.xml",
]

SEO_JS_IGNORE_EXTENSIONS = [
    ".xml",
    ".txt",
    # See helpers.py for full list of extensions ignored by default.
]

# Prerender.io token
SEO_JS_PRERENDER_TOKEN = "123456789abcdefghijkl"

SEO_JS_BACKEND = "django_seo_js.backends.PrerenderHosted"
SEO_JS_PRERENDER_URL = "http://my-prerenderapp.com/"  # Note trailing slash.
SEO_JS_PRERENDER_RECACHE_URL = "http://my-prerenderapp.com/recache"

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
TEST_RUNNER = 'django_selenium.selenium_runner.SeleniumTestRunner'

FEED_UPDATE_CELERY = True

PIPELINE_COMPILERS = (
  'pipeline.compilers.less.LessCompiler',
)

DEFAULT_INDEX_TABLESPACE = ''

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.BaseSignalProcessor'

HAYSTACK_CONNECTIONS = {
   'default': {
   'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
   'URL': 'http://127.0.0.1:8983/solr'
   },
}

CSS_URL = '/var/www/vhosts/zrealtycorp.com/zrealty/static/css'


GRAPPELLI_ADMIN_TITLE = 'ZRealty Corp'

GRAPPELLI_INDEX_DASHBOARD = {
   'django.contrib.admin.site': 'zrealty.dashboard.CustomIndexDashboard',
}
PAGING_PAGE_SIZE = 10

# Email settings
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'allseeingeye1003@gmail.com'
EMAIL_HOST_PASSWORD = 'nu45edi1'
DEFAULT_FROM_EMAIL = 'info@zrealtycorp.com'
DEFAULT_TO_EMAIL = 'dmitryro@gmail.com'
ACCOUNT_ACTIVATION_DAYS=7

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_ERROR_URL = '/login/'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
TEST_GOOGLE_USER = 'dmitryro@gmail.com'
TEST_GOOGLE_PASSWORD = 'nu45edi1'
REGISTRATION_API_ACTIVATION_SUCCESS_URL = '/'
# Social Authentication Settings
APPEND_SLASH = True

SOCIAL_AUTH_PIPELINE = (
  'social_auth.backends.pipeline.social.social_auth_user',
  'social_auth.backends.pipeline.associate.associate_by_email',
  'social_auth.backends.pipeline.misc.save_status_to_session',
  'social_auth.backends.pipeline.social.associate_user',
  'social_auth.backends.pipeline.social.load_extra_data',
  'social_auth.backends.pipeline.user.update_user_details',
)
