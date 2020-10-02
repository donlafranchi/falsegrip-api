from django.db import models
from django.conf import settings

from .mixins import *


class Equipment(UUIDPrimaryKeyMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Trainer(UUIDPrimaryKeyMixin):
    name = models.CharField(max_length=100)
    website_url = models.CharField(max_length=250, null=True, blank=True)
    instagram_url = models.CharField(max_length=250, null=True, blank=True)
    youtube_url = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Muscle(UUIDPrimaryKeyMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Exercise(UUIDPrimaryKeyMixin, CreatedModifiedMixin):

    CATEGORY = (
        ('Push', 'Push'),
        ('Pull', 'Pull'),
        ('Legs', 'Legs'),
        ('Core', 'Core'),
        ('Other', 'Other')
    )

    TYPE = (
        ('Compound', 'Compound'),
        ('Corrective', 'Corrective'),
        ('Warmup', 'Warmup')
    )

    DIFFICULTY_LEVEL = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    )

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(default='rings_default.jpg')
    short_demo = models.FileField(null=True, blank=True)
    instruction_video = models.CharField(max_length=250, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    equipments = models.ManyToManyField(Equipment, blank=True)
    muscle_target = models.ManyToManyField(Muscle, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY)
    type = models.CharField(max_length=50, choices=TYPE, null=True, blank=True)
    difficulty_level = models.CharField(max_length=50, choices=DIFFICULTY_LEVEL)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Workout(UUIDPrimaryKeyMixin, CreatedModifiedMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workouts")
    datetime = models.DateTimeField()
    title = models.CharField(max_length=250)
    body_weight = models.FloatField(null=True, blank=True)
    energy_level = models.IntegerField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    exercises = models.ManyToManyField(Exercise, blank=True)
    order = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('datetime',)

    def __str__(self):
        return f'{self.user.username} - {self.datetime.strftime("%m/%d/%Y %H:%M")}'


class Set(CreatedModifiedMixin):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="sets")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sets')
    num = models.IntegerField()
    reps = models.IntegerField()

    class Meta:
        ordering = ('num',)

    def __str__(self):
        return str(self.num)
