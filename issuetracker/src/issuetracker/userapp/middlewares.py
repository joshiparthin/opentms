from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User

def simple_middleware(get_response):
    def middleware(request):
        print("checking", request.path)
        # print ("namespaces", request.resolver_match.namespaces)

        if not request.path in settings.ALLOWED_URLS_WITHOUT_SESSIONS:
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Not allowed to use the system <a href='/user/login'>Login here</a>")
        return get_response(request)

    return middleware