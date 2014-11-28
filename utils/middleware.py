from django.contrib.auth import logout

class ForceLogoutMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            logout(request)
