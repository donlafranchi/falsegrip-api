import time

from rest_framework import permissions, status, viewsets
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum

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
    ordering_fields = ('created', 'datetime')
    ordering = ('-datetime', )

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
    # ordering_fields = ('name', 'order')
    # ordering = ('order',)
    filterset_fields = ('category', 'type', 'difficulty_level', 'active')
    search_fields = ('name',)
    queryset = Exercise.objects.filter(active=True)

    @action(detail=True, methods=['GET'])
    def history(self, request, *args, **kwargs):
        exercise = self.get_object()
        serializer = ExerciseSerializer(exercise)
        data = serializer.data

        personal_record = 0
        total_reps = 0
        history = {}

        workouts = request.user.workouts.filter(exercises__id__exact=exercise.id)
        if workouts:
            sets = exercise.sets.filter(workout__in=workouts).order_by('-reps')
            max_set = sets.first()
            if max_set:
                personal_record = max_set.reps

            total_reps = sets.aggregate(Sum('reps'))['reps__sum'] or 0

            x = 12
            now = time.localtime()
            months = [time.localtime(time.mktime((now.tm_year, now.tm_mon - n, 1, 0, 0, 0, 0, 0, 0)))[:2] for n in range(x)]

            for month in months:
                _workouts = workouts.filter(datetime__year=month[0], datetime__month=month[1]).order_by('-datetime')
                if not _workouts:
                    continue

                records = []
                for wo in _workouts:
                    reps = wo.sets.filter(exercise=exercise).aggregate(Sum('reps'))['reps__sum'] or 0
                    records.append({wo.datetime.strftime('%d %a'): reps})

                history[f'{month[0]}-{month[1]}'] = records

        data['personal_record'] = personal_record
        data['total_reps'] = total_reps
        data['history'] = history

        return Response(data, status=201)


class SetViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = SetSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filterset_fields = ('exercise',)
    queryset = Set.objects.all()
