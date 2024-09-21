from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..serializers.role import RoleSerializer
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password', 'avatar_url']

        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  
        validated_data['status'] = 1
        validated_data['email_verified'] = False  
        user = User.objects.create(**validated_data)
        return user
