from django import forms
from django import template
from django.forms import ModelForm
from django.template import loader, Context
from django.core.context_processors import media as media_processor
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from property.models import Property, Borough, Neighborhood
from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey
register = template.Library()


#from uni_form.helper import FormHelper

class SearchErrorList(list):
    def get(self, request):
        pass
    class Meta:
        def __init__(self, *args, **kwargs):
            pass



class SearchForm(NgFormValidationMixin, NgModelFormMixin, ModelForm):
    form_name = 'property_form'
#    max_price = forms.IntegerField(min_value=0, required=False, initial=0)
#    min_price = forms.IntegerField(min_value=0, required=False, initial=0)
    min_price = forms.DecimalField(min_value=0, max_value=1000000000,required=False, initial=0)
    max_price = forms.DecimalField(min_value=0, max_value=1000000000,required=False, initial=0)


    class Meta:
        model = Property
        fields = ['rooms', 'type', 'category', 'borough','neighborhood','min_price','max_price','pets_allowed']

        def __init__(self, *args, **kwargs):

            super(SearchForm, self).__init__(*args, **kwargs)
            self.fields['rooms'].widget.attrs.update({'class' : 'search-panel-field'})
            self.fields['type'].widget.attrs.update({'class' : 'search-panel-field'})
            self.fields['category'].widget.attrs.update({'class' : 'search-panel-field'})

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
      #  raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

    def form_invalid(self, form):
        if self.request.is_ajax():
            to_json_responce = dict()
            to_json_responce['status'] = 0
            to_json_responce['form_errors'] = form.errors

            return HttpResponse(json.dumps(to_json_responce), content_type='application/json')

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            to_json_responce = dict()
            to_json_responce['status'] = 1

            return HttpResponse(json.dumps(to_json_responce), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(SearchForm, self).get_context_data(**kwargs)
        context.update(contact_form=SearchForm())
        context['search_call']='yes'
        return context


property_form = SearchForm()
