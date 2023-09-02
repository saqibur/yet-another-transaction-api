# Standard library imports

# Django imports
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import (
    AuthenticationFailed,
    NotAuthenticated,
)

# Third party imports
from decouple import config

# Local imports


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        x_api_key = request.META.get("HTTP_X_API_KEY")

        if x_api_key is None:
            raise NotAuthenticated
        elif x_api_key != config("API_KEY"):
            raise AuthenticationFailed
        else:
            return None, True
