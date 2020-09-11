from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView

from .serializers import RegisterSerializer, LoginSerializer


class CustomRegisterView(RegisterView):
    serializer_class = RegisterSerializer


class CustomLoginView(LoginView):
    serializer_class = LoginSerializer
