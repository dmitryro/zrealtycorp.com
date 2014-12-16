from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from rest_framework import viewsets, routers
from tastypie.api import Api
from feeds.feeds import RssSiteNewsFeed, AtomSiteNewsFeed
from ajax_select import urls as ajax_select_urls
from property.views import PropertyListView
from property.views import PropertyView
from property.views import SearchFormView
from property.views import SalesList, RentList
from dashboard.views import DashboardView
from dashboard.views import DashboardLogoutView
from utils.views import MemberLoginView
from utils.views import MemberSignupView
from utils.models import Member
from pages.views import MaintenanceView
from pages.views import PropertyDetailView 
from pages.views import HomeView
from pages.views import AboutView
from pages.views import ContactView
from pages.views import BlogView
from pages.views import MobileView
from pages.views import FeaturedView
from pages.views import RentView
from pages.views import SalesView
from pages.views import AgentView
from pages.views import RssView
from api import views
import rest_auth
import rules_light
import autocomplete_light
import smart_selects
import socialregistration
import podcast

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class MemberViewSet(viewsets.ModelViewSet):
    model = Member



# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'members', MemberViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'properties',views.PropertyViewSet)
router.register(r'categories',views.CategoryViewSet)
router.register(r'types',views.TypeViewSet)
router.register(r'statuses',views.StatusViewSet)
router.register(r'neighborhoods',views.NeighborhoodViewSet)
router.register(r'boroughs',views.BoroughViewSet)
router.register(r'rooms',views.RoomsViewSet)


rules_light.autodiscover()
autocomplete_light.autodiscover()
admin.autodiscover()

feeds = {
    'rss': RssSiteNewsFeed,
    'atom': AtomSiteNewsFeed,
}


urlpatterns = patterns('',
    url(r'^home/$', HomeView.as_view()),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^complete/google-oauth2/', RedirectView.as_view(url='/dashboard/')),
    url(r'^accounts_api/', include('registration_api.urls')),
    url(r'^accounts/login/',RedirectView.as_view(url='/dashboard/')),
    url(r'^$',HomeView.as_view()),
    url(r'^rest/$', RedirectView.as_view(url='/rest/login')),
    url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="buttons"),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/property/neighborhood/add/$',include('smart_selects.urls')),
    url(r'^blog/', BlogView.as_view()),
    url(r'^mobile/', MobileView.as_view()),
    url(r'^post/$', views.EmailView.as_view()), #this endpoint is used to send emails
    url(r'^notifynew/$', views.NotifyView.as_view()), #this endpoint is used to send emails
    url(r'^sale/', SalesView.as_view()),
    url(r'^sales/', SalesView.as_view()),
    url(r'^rent/', RentView.as_view()),
    url(r'^contact/', ContactView.as_view()),
    url(r'^contactus/', views.ContactView.as_view()),
    url(r'^featured/', FeaturedView.as_view()),
    url(r'^rentals/', RentView.as_view()),
    url(r'^agents/', AgentView.as_view()),
    url(r'^about/', AboutView.as_view()),
    url(r'^dashboard/', DashboardView.as_view()),
    url(r'^logout/',DashboardLogoutView.as_view()),
    url(r'^search/', views.SearchView.as_view()),
    url(r'^rss/', RssSiteNewsFeed()),
    url(r'^atom/', AtomSiteNewsFeed()),
    url(r'^signup/',MemberSignupView.as_view()),
    url(r'^signin/',MemberLoginView.as_view()), 
#    url(r'^accounts/login/$',MemberLoginView.as_view()),
    url(r'^accounts/login/$',RedirectView.as_view(url='/signin/')),
    url(r'^podcasts/', include('podcast.urls')),
    url(r'^properties/(?P<type_id>[0-9a-zA-Z_-]+)/$',PropertyListView.as_view(),
        name='property_type_list'
    ),
    url(r'^saleslist/$',SalesList.as_view()),
    url(r'^rentlist/$',RentList.as_view()),
    url(r'^property/(?P<property_id>[0-9]+)', PropertyDetailView.as_view(),
        name='property_detail'
    ),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
    url(r'^properties/(?P<type>.+)/$', views.PropertyTypeViewSet.as_view({
      'get': 'list'
    }
    )),
    url(r'^categories/(?P<type>.+)/$', views.CategoryViewSet.as_view({
      'get': 'list'
    }
    )),

    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/', include(admin.site.urls)),
    url(r'^admin/property/',include(admin.site.urls)),
    url(r'^admin/property/borough/$',include(admin.site.urls)),
    url(r'^admin/property/location/$',include(admin.site.urls)),   
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^complete/google-oauth2/', RedirectView.as_view(url='/dashboard/')),
    url(r'^complete/twitter/?oauth_token$',RedirectView.as_view(url='/dashboard/')),
    url(r'^accounts/login/',RedirectView.as_view(url='/dashboard/')),
    url(r'^rest/$', RedirectView.as_view(url='/rest/login')),
    url(r'^login/$', RedirectView.as_view(url='/rest/login')),
    url(r'^ogin/$', RedirectView.as_view(url='/rest/login')),
    url(r'^gin/$', RedirectView.as_view(url='/rest/login')),
    url(r'^in/$', RedirectView.as_view(url='/rest/login')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="buttons"),
    url(r'^facebook_login/xd_receiver.htm$', TemplateView.as_view(template_name='socialauth/xd_receiver.htm'), name='socialauth_xd_receiver'),
    url(r'^facebook_login/$', 'facebook_login', name='socialauth_facebook_login'),
    url(r'^facebook_login/done/$', 'facebook_login_done', name='socialauth_facebook_login_done'),
    url(r'^login/$', 'login_page', name='socialauth_login_page'),
    url(r'^openid_login/$', 'openid_login_page', name='socialauth_openid_login_page'),
    url(r'^twitter_login/$', 'twitter_login', name='socialauth_twitter_login'),
    url(r'^twitter_login/done/$', 'twitter_login_done', name='socialauth_twitter_login_done'),
    url(r'^linkedin_login/$', 'linkedin_login', name='socialauth_linkedin_login'),
    url(r'^linkedin_login/done/$', 'linkedin_login_done', name='socialauth_linkedin_login_done'),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^feedreader/', include('feedreader.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/property/neighborhood/add/$',include('smart_selects.urls')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'/property/(?P<slug>\w+)/$', PropertyView.as_view(), name='property_view'),
    url(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
    url(r'^social/', include('socialregistration.urls',namespace = 'socialregistration')),
    url(r'^', include(router.urls)),
    url(r'', include('social_auth.urls')),
   # url(r'^', include(router.urls)),
)

