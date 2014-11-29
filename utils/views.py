from django.forms.formsets import formset_factory
from django.views.generic import TemplateView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, AbstractUser
from rest_framework.authtoken.models import Token
from forms import MemberLoginForm, MemberForm
from property.forms import SearchForm
from serializers import UserSerializer, MemberSerializer
from models import Member


for user in User.objects.all():
    Token.objects.get_or_create(user=user)

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        users = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)




# Create your views here.
"""
  Member Login  View Mixing
"""
class LoginViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(LoginViewMixin,
                  self).get_context_data(**kwargs)

        form = MemberLoginForm()
        context['member_login_form'] = form
        sform =  SearchForm()
        context['property_form'] = sform

        return context

"""
  Signup View Mixing
"""
class SignupViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(SignupViewMixin,
                  self).get_context_data(**kwargs)

        form = MemberForm()
        context['member_form'] = form
        sform =  SearchForm()
        context['property_form'] = sform

        return context


"""
  Login View 
"""

class MemberLoginView(LoginViewMixin, TemplateView):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(MemberLoginView, self).dispatch(*args, **kwargs)
    template_name = "signin.html"


"""
  Signup visitor view
"""
class MemberSignupView(SignupViewMixin, TemplateView):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(MemberSignupView, self).dispatch(*args, **kwargs)
 
    template_name = "register.html"


"""
  Registration API view
"""
class RegistrationView(APIView):

    passsion_classes = ()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.DATA)

        # Check format and unique constraint
        if not serializer.is_valid():
            return Response(serializer.errors,\
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        u = User.objects.create(username=data['username'])
        u.set_password(data['password'])
        u.save()

        # Create OAuth2 client
        name = u.username
        client = Client(user=u, name=name, url='' + name,\
                client_id=name, client_secret='', client_type=1)
        client.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
