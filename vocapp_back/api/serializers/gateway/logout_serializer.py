from rest_framework import serializers
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout
from rest_framework.validators import UniqueValidator


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        request = self.context.get('request')

        # This is for debugging purposes only.
        print(username, password)

        try:
            return authenticate(username=username, password=password) # Output us a "User" object
        except Exception as e:
            print(e)
        raise serializers.ValidationError({
             'message': 'Could not log in, username or password are incorrect.'
        })
