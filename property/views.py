"""
Created on Jul 6, 2014
@author: Dmitry Roitman
"""

from django.http import HttpResponse
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from djangular.views.mixins import JSONResponseMixin, allow_remote_invocation
from property.models import Property
from property.serializers import PropertySerializer
from property.serializers import CategorySerializer
from forms import SearchForm

class PropertyList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        properties = Property.objects.all()
        serializer = PropertySerializer(property, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def property_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Property.objects.all()
        serializer = PropertySerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PropertySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

class PropertyViewMixin(object):
    pass

class PropertyListViewMixin(object):
    pass


class SearchActionMixin(object):
    @property
    def action(self): 
        pass

    def valid(self,form):
        pass      
 
class SearchFormView(TemplateView):
    template_name="search.html"
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(SearchFormView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest('Expected an XMLHttpRequest')
        in_data = json.loads(request.body)
        bound_property_form = CheckoutForm(data={'pets_allowed': in_data.get('pets_allowed')})
        # now validate .bound_contact_form. and use it as in normal django

    def get_context_data(self, **kwargs):
        context = super(SearchFormView, self).get_context_data(**kwargs)
        context.update(property_form=SearchForm())
        return context

class SearchUpdateView(SearchActionMixin,TemplateView):
    def get_context_data(self, **kwargs):
        context = super(SearchFormView, self).get_context_data(**kwargs)
        context.update(property_form=SearchForm())
        context['search_call']='yes'
        return context

class SearchCreateView(SearchActionMixin,TemplateView):
    def get_context_data(self, **kwargs):
        context = super(SearchFormView, self).get_context_data(**kwargs)
        context.update(property_form=SearchForm())
        context['search_call']='yes'
        return context


class PropertyView(PropertyViewMixin, TemplateView):
    template_name = "property.html"

class PropertyListView(PropertyListViewMixin, TemplateView):
    template_name = "property.html"


class SalesList(generics.ListAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        filter_fields = ('category_id',2)
        return Property.objects.filter(filter_fields)

class RentList(generics.ListAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        filter_fields = ('category_id',1)
        return Property.objects.filter(filter_fields)

