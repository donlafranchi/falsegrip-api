from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView

from .serializers import *


class CustomRegisterView(RegisterView):
    serializer_class = RegisterSerializer


class CustomLoginView(LoginView):
    serializer_class = LoginSerializer
