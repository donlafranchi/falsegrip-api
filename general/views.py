from rest_framework import permissions, status, viewsets
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework_extensions.mixins import NestedViewSetMixin

from .serializers import *


class CustomRegisterView(RegisterView):
    serializer_class = RegisterSerializer


class CustomLoginView(LoginView):
    serializer_class = LoginSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = Workout.objects.all()
    search_fields = ('title',)

    def get_queryset(self):
        qs = super(WorkoutViewSet, self).get_queryset()
        qs = qs.filter(user=self.request.user)

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExerciseViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filterset_fields = ('equipment', 'primary_muscle')
    search_fields = ('name', 'creators')
    queryset = Exercise.objects.all()


class SetViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = SetSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filterset_fields = ('exercise',)
    queryset = Set.objects.all()
