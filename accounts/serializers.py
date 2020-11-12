from rest_framework import serializers

from .models import AppUser


class RegisterSerializer(serializers.Serializer):
    apple_id = serializers.CharField()
    first_name = serializers.CharField()

    def validate(self, data):
        if AppUser.objects.filter(username=data['apple_id']).exists():
            raise serializers.ValidationError("The user already exists.")
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('apple_id', ''),
            'first_name': self.validated_data.get('first_name', ''),
        }

    def save(self, request):
        self.cleaned_data = self.get_cleaned_data()
        user = AppUser(username=self.cleaned_data['username'], first_name=self.cleaned_data['first_name'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    apple_id = serializers.CharField()

    def validate(self, attrs):
        apple_id = attrs.get('apple_id')
        user = AppUser.objects.filter(username=apple_id).first()
        if not user:
            msg = 'Unable to log in with provided credentials.'
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs
