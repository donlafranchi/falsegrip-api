from django.db import models

from .mixins import *


class Workout(UUIDPrimaryKeyMixin, CreatedModifiedMixin):
    datetime = models.DateTimeField()
    title = models.CharField(max_length=250)
    body_weight = models.FloatField(null=True, blank=True)
    energy_level = models.IntegerField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="workouts")


class Excercise(UUIDPrimaryKeyMixin, CreatedModifiedMixin):
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

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
    image = models.FileField()
    gif = models.FileField(null=True, blank=True)
    video = models.CharField(max_length=250, null=True, blank=True)
    creators = models.TextField(null=True, blank=True)
    equipment = models.CharField(max_length=50, choices=EQUIPMENT)
    primary_muscle = models.CharField(max_length=50, choices=MUSCLE)
    secondary_muscle = models.CharField(max_length=50, choices=MUSCLE, null=True, blank=True)


class Set(UUIDPrimaryKeyMixin, CreatedModifiedMixin):
    exercise = models.ForeignKey(Excercise, on_delete=models.CASCADE, related_name='sets')
    num = models.IntegerField()
    reps = models.IntegerField()
