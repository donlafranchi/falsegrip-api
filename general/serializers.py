from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class RegisterSerializer(serializers.Serializer):
    apple_id = serializers.CharField()
    first_name = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['apple_id']).exists():
            raise serializers.ValidationError("The user already exists.")
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('apple_id', ''),
            'first_name': self.validated_data.get('first_name', ''),
        }

    def save(self, request):
        self.cleaned_data = self.get_cleaned_data()
        user = User(username=self.cleaned_data['username'], first_name=self.cleaned_data['first_name'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    apple_id = serializers.CharField()

    def validate(self, attrs):
        apple_id = attrs.get('apple_id')
        user = User.objects.filter(username=apple_id).first()
        if not user:
            msg = 'Unable to log in with provided credentials.'
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs


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
