# project/settings.py:
ACCOUNT_ADAPTER = 'project.users.adapter.UserAccountAdapter'

# project/users/adapter.py:
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class UserAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/dashboard/"
        return path.format(username=request.user.username)

class LoginAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/accounts/{username}/"
        return path.format(username=request.user.username)
