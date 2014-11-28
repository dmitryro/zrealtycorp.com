from django import forms
from django import template
from django.forms import ModelForm
from django.template import loader, Context
from django.core.context_processors import media as media_processor
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from utils.models import Member, Login
#from uni_form.helper import FormHelper

class MemberErrorList(list):
    def get(self, request):
        pass
    class Meta:
        def __init__(self, *args, **kwargs):
            pass

class MemberLoginErrorList(list):
    def get(self, request):
        pass
    class Meta:
        def __init__(self, *args, **kwargs):
            pass

"""
  Member login form
"""
class MemberLoginForm(NgFormValidationMixin, NgModelFormMixin, ModelForm):
    form_name = 'member_login_form'

    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='login')
        super(MemberLoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Login
        fields = ['username','password']
        widgets = {
            'password': forms.PasswordInput(),
        }


        def __init__(self, *args, **kwargs):

            super(MemberLoginForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class' : 'search-panel-field','ng-model': 'login.email'})
            self.fields['password'].widget.attrs.update({'class' : 'search-panel-field', 'ng-model': 'login.password'})

    def clean(self):
        cleaned_data = super(MemberLoginForm, self).clean()
        email = cleaned_data.get("username")
        password = cleaned_data.get("password")

    def clean_email(self):
        data = self.cleaned_data['username']
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        return data

 
    def form_invalid(self, form):
        pass

    def form_valid(self, form):
        pass


"""
  New member registration form
"""
class MemberForm(NgFormValidationMixin, NgModelFormMixin, ModelForm):
    form_name = 'member_form'

    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='member')
        super(MemberForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Member
        fields = ['username','password','confirm_password','email']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

        def __init__(self, *args, **kwargs):

            super(MemberForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class' : 'search-panel-field'})  
            self.fields['password'].widget.attrs.update({'class' : 'search-panel-field'}) 
            self.fields['confirm_password'].widget.attrs.update({'class' : 'search-panel-field'})
            self.fields['email'].widget.attrs.update({'class' : 'search-panel-field'})

    def clean(self):
        cleaned_data = super(MemberForm, self).clean()
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


member_login_form = MemberLoginForm()
member_form = MemberForm()
