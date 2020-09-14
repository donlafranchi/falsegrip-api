from django.db import models
from django.conf import settings

from .mixins import *


class Workout(UUIDPrimaryKeyMixin, CreatedModifiedMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workouts")
    datetime = models.DateTimeField()
    title = models.CharField(max_length=250)
    body_weight = models.FloatField(null=True, blank=True)
    energy_level = models.IntegerField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.user.username} - {self.datetime.strftime("%m/%d/%Y %H:%M")}'


class Exercise(UUIDPrimaryKeyMixin, CreatedModifiedMixin):
    EQUIPMENT = (
        ('Rings', 'Rings'),
        ('Bar', 'Bar'),
        ('Floor', 'Floor'),
    )

    MUSCLE = (
        ('Back', 'Back'),
        ('Chest', 'Chest'),
        ('Shoulder', 'Shoulder'),
        ('Bicep', 'Bicep'),
        ('Tricep', 'Tricep'),
        ('Legs', 'Legs'),
        ('Abs', 'Abs')
    )

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="media")
    gif = models.FileField(upload_to="media", null=True, blank=True)
    video = models.CharField(max_length=250, null=True, blank=True)
    creators = models.TextField(null=True, blank=True)
    equipment = models.CharField(max_length=50, choices=EQUIPMENT)
    primary_muscle = models.CharField(max_length=50, choices=MUSCLE)
    secondary_muscle = models.CharField(max_length=50, choices=MUSCLE, null=True, blank=True)

    class Meta:
        ordering = ('created',)


class Set(CreatedModifiedMixin):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sets')
    reps = models.IntegerField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.id)
