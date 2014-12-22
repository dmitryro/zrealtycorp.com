from django import forms
from django import template
from django.forms import ModelForm
from django.template import loader, Context
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from models import PrivateMessage

class MessageForm(NgFormValidationMixin, NgModelFormMixin,forms.ModelForm):
#    title = forms.CharField(max_length=200)
    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='private')
        super(MessageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PrivateMessage
        fields = ['receiver','title','message']


