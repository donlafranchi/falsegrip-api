from django.contrib import admin

from .models import *


class SetAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'reps')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'equipment', 'primary_muscle', 'secondary_muscle')
    list_filter = ('equipment', 'primary_muscle')
    # search_fields = ('suite', 'property__name',)
    # autocomplete_fields = ('property',)
    # inlines = (SetAdmin,)


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime', 'title')
    # list_filter = ('equipment', 'primary_muscle')
    # search_fields = ('suite', 'property__name',)
    # autocomplete_fields = ('property',)


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Set, SetAdmin)
