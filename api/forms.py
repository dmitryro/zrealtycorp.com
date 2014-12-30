from django import forms
from django import template
import provider.forms.OAuthForm
import provider.forms.OAuthValidationError

class GrantValidationForm(OAuthForm):
    grant_type = forms.CharField()

    def clean_grant(self):
        if not self.cleaned_data.get('grant_type') == 'code':
            raise OAuthValidationError({
                'error': 'invalid_grant',
                'error_description': "%s is not a valid grant type" % (
                    self.cleaned_data.get('grant_type'))
            })
