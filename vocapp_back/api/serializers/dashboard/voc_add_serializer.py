from rest_framework import serializers
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout
from rest_framework.validators import UniqueValidator


class VocaddSerializer(serializers.Serializer):
    word = serializers.CharField()
    explantation = serializers.CharField()
    def create(self, validated_data):
        word = validated_data.get('word')
        explantation = validated_data.get('explantation')
        request = self.context.get('request')

        # This is for debugging purposes only.
        print(word, explantation)
        user = User.objects.create_user(word,explantation)
        user.word = word
        user.explantation = explantation
        user.save()
        return user
