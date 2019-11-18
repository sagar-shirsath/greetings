# from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
# from edx_rest_framework_extensions.auth.session.authentication import SessionAuthenticationAllowInactiveUser
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication


def view_auth_classes():

    def _decorator(func_or_class):
        func_or_class.authentication_classes = [ TokenAuthentication ]
        func_or_class.permission_classes = (IsAuthenticated,)
        func_or_class.allowed_methods = ('GET','POST')

        return func_or_class
    return _decorator
