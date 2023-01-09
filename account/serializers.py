from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class RegisterAbstractSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'is_sender']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('пароли должны совпадать')
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(user=user,
                                         is_sender=validated_data['is_sender'])
        return user


class SenderRegisterSerializer(RegisterAbstractSerializer):
    is_sender = serializers.BooleanField(default=True)


class BuyerRegisterSerializer(RegisterAbstractSerializer):
    is_sender = serializers.BooleanField(default=False)


