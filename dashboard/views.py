from django.shortcuts import render
from django.views.generic import TemplateView
from braces import views
from braces.views import AnonymousRequiredMixin
from braces.views import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpRequest
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from utils.forms import MemberLoginForm
from property.forms import SearchForm


class DashboardViewMixin(object):

    def get_context_data(self,**kwargs):
        context = super(DashboardViewMixin,
                  self).get_context_data(**kwargs)
        user = HttpRequest.user
        context['user'] = user
        return context


class DashboardLogoutViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(DashboardLogoutViewMixin,
                  self).get_context_data(**kwargs)
        form = MemberLoginForm()
        context['member_login_form'] = form
        sform =  SearchForm()
        context['property_form'] = sform
        return context


class DashboardView(LoginRequiredMixin, DashboardViewMixin, TemplateView):
    template_name = "dashboard.html"
    
    def get(self, request):
        if not request.user.is_authenticated():
            #return render_to_response('signin.html')  
            return render_to_response('signin.html', c, context_instance=RequestContext(request)) 

        return render(request, 'dashboard.html')


class DashboardLogoutView(LoginRequiredMixin, DashboardLogoutViewMixin, TemplateView):
    template_name = "signin.html"
    def get(self, request):
 #       if request.user.is_authenticated(): 
        logout(request)
        form = MemberLoginForm()
        return render(request,'signin.html',{'member_login_form':form})

