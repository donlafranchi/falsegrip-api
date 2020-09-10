from django.db import models

from .mixin import *


class Workout(UUIDPrimaryKeyMixin, CreatedModifiedMixin):
    body_weight = models.FloatField()
    energy_level = models.IntegerField()
    comments = models.TextField(null=True, blank=True)
    user = models.OnetoOneKey("User")


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
    description = models.TextField()
    workout = models.ForeignKey(Workout, related_name="exercises")
    image = models.FileField()
    gif = models.FileField()
    video_url = models.CharField(max_length=250)
    equipment = models.CharField(max_length=50, choices=EQUIPMENT, null=True, blank=True)
    primary_muscle = models.CharField(max_length=50, choices=MUSCLE)
    secondary_muscle = models.CharField(max_length=50, choices=MUSCLE, null=True, blank=True)
