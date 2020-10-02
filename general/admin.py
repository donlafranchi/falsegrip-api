from django.contrib import admin

from .models import *


class SetAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'reps')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'type', 'difficulty_level', 'active')
    list_filter = ('category', 'active', 'type', 'difficulty_level')


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime', 'title')


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MuscleAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Set, SetAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Muscle, MuscleAdmin)
