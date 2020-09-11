from django.contrib.auth.models import User
from rest_framework import serializers

class CustomRegisterSerializer(serializers.Serializer):
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
