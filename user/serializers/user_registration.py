from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..services.user import generate_email_verification_token
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'email_verified']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            role=validated_data.get('role', 'default_role'),
        )
        user.set_password(validated_data['password'])
        user.save()

        # Tạo token xác thực email và gửi email
        token = generate_email_verification_token(user)
        verification_url = reverse('verify-email', kwargs={'token': token})
        verification_link = f"http://localhost:8000{verification_url}"

        # Gửi email xác thực
        send_mail(
            'Verify your email',
            f'Click the following link to verify your email: {verification_link}',
            'your-email@example.com',
            [user.email],
            fail_silently=False,
        )
        
        return user
