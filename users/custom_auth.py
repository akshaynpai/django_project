from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from users.models import *

class CustomAuthenticationBackend(BaseBackend):
    
   def authenticate(self, request):
        # Get the token from the request header or query parameters
        token_string = request.META.get('HTTP_AUTHORIZATION') or request.GET.get('token')
        token = token_string.split(" ")[1]
        if not token:
            return Response({"Message":"Token Missing"},status=401)

        try:
            # Find the user associated with the token
            user = Employees.objects.get(api_token=token)
            return (user, None)
        except Employees.DoesNotExist:
            return Response({"Message":"Invalid Token"},status=401)

    