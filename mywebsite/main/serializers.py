from rest_framework import serializers
from .models import Country, Address, UserAddress
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name ', 'email', 'password']


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user