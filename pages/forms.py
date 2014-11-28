# -*- coding: utf-8 -*-
from django import forms
from django import template
from models import ContactPage
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from property.models import Property,Borough,Neighborhood

register = template.Library()


#from uni_form.helper import FormHelper

class ContactErrorList(list):
    pass


class ContactForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
    name = forms.CharField(
        max_length=100,
        help_text=u'',
    )

    email = forms.EmailField()

    subject = forms.ChoiceField(
        choices=(
            ("request", "Request info"),
            ("feedback", "Send a feedback"),
            ("meetup", "Request an appointment"), 
        ),
        help_text=u'',
    )


    message = forms.CharField(
        max_length=1000,
        help_text=u'',
        widget=forms.Textarea(
            attrs={
                'Message': '',
            }
        ),
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
      #  raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

    def form_invalid(self, form):
        if self.request.is_ajax():
            to_json_responce = dict()
            to_json_responce['status'] = 0
            to_json_responce['form_errors'] = form.errors

     #       to_json_responce['new_cptch_key'] = CaptchaStore.generate_key()
      #      to_json_responce['new_cptch_image'] = captcha_image_url(to_json_responce['new_cptch_key'])

            return HttpResponse(json.dumps(to_json_responce), content_type='application/json')

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            to_json_responce = dict()
            to_json_responce['status'] = 1

            to_json_responce['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_responce['new_cptch_image'] = captcha_image_url(to_json_responce['new_cptch_key'])
            return HttpResponse(json.dumps(to_json_responce), content_type='application/json')

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        field = ('name','email', 'subject', 'message')


class SearchForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
    
    borough = forms.ModelMultipleChoiceField(queryset=Borough.objects.all())
    
    class Meta:
        model = Property
        field = ('borough')

inquiry_form = SearchForm(form_name='inquiry_form', scope_prefix='inquiry_model')
contact_form = ContactForm(form_name='contact_form', scope_prefix='contact_model')

