from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework import status, views, viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action

from .permissions import BaseUserPermission
from .serializers import *


class CustomRegisterView(RegisterView):
    serializer_class = RegisterSerializer


class CustomLoginView(LoginView):
    serializer_class = LoginSerializer


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
    def from_token(self, request, *args, **kwargs):
        """
        Returns the user associated with the provided token.
        Provided as a convenience function for easily retrieving users from
        the frontend when all they have is a token.
        """
        token_string = request.query_params.get('token')
        if not token_string:
            return GenericErrorResponse('Token query parameter is required')
        token = get_object_or_404(Token, key=token_string)
        self.kwargs['pk'] = token.user_id
        user = self.get_object()
        return Response(self.get_serializer(user).data)
