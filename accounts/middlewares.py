from django.contrib.auth import logout
from django.http import HttpResponseForbidden


class ActivatedAccountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_authenticated or request.user.is_active:
            return self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        logout(request.user)

        return HttpResponseForbidden("You are not activated yet! Please contact site admin")
