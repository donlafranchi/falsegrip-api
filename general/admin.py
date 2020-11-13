from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import *


class SetAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'reps')


class ExerciseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'category', 'type', 'difficulty_level', 'active')
    list_filter = ('category', 'active', 'type')


class WorkoutAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('user', 'datetime', 'title')


class EquipmentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)


class TrainerAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)


class MuscleAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Set, SetAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Muscle, MuscleAdmin)
