from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework import status, views, viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from .permissions import BaseUserPermission
from .serializers import *


class CustomRegisterView(RegisterView):
    serializer_class = RegisterSerializer


class CustomLoginView(LoginView):
    serializer_class = LoginSerializer


class GenericErrorResponse(Response):
    def __init__(self, message):
        # Ensure that the message always gets to the user in a standard format.
        if isinstance(message, ValidationError):
            message = message.detail
        if isinstance(message, str):
            message = [message]
        super().__init__({"non_field_errors": message}, status=400)


class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    permission_classes = (BaseUserPermission,)

    def get_queryset(self):
        return get_user_model().objects.all()

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        return Response(self.get_serializer(request.user).data)
