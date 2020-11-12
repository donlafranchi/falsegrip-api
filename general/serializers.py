from rest_framework import serializers

from .models import *


class WorkoutSerializer(serializers.ModelSerializer):
    exercises_obj = serializers.SerializerMethodField()

    def get_exercises_obj(self, obj):
        context = { 'workout': obj.id }
        exercises = obj.exercises
        if obj.order:
            exercises = []
            ids = obj.order.split(',')
            for pk in ids:
                item = obj.exercises.filter(pk=pk).first()
                if item:
                    exercises.append(item)

        data = ExerciseSerializer(exercises, many=True, context=context).data

        return data

    class Meta:
        model = Workout
        exclude = ('user',)


class ExerciseSerializer(serializers.ModelSerializer):
    sets = serializers.SerializerMethodField()
    trainer_obj = serializers.SerializerMethodField()
    equipments_obj = serializers.SerializerMethodField()
    muscle_target_obj = serializers.SerializerMethodField()

    def get_sets(self, obj):
        if self._context and self._context.get('workout'):
            sets = obj.sets.filter(workout=self._context.get('workout'))
            data = SetSerializer(sets, many=True).data

            return data

    def get_trainer_obj(self, obj):
        data = TrainerSerializer(obj.trainer).data

        return data

    def get_equipments_obj(self, obj):
        data = EquipmentSerializer(obj.equipments, many=True).data

        return data

    def get_muscle_target_obj(self, obj):
        data = MuscleSerializer(obj.muscle_target, many=True).data

        return data

    class Meta:
        model = Exercise
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = '__all__'


class MuscleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Muscle
        fields = '__all__'
