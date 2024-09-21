from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from ..serializers import UserSerializer
from rest_framework import permissions, viewsets, renderers
from user.models.user import User
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework import permissions
from ..permissions import IsOwner
from ..services.user import verify_email_verification_token, send_verification_email

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    max_page_size = 1000


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=['post'], url_path='perform-create', detail=True, permission_classes=[permissions.AllowAny], 
            renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['post'], url_path='register', detail=False, permission_classes=[permissions.AllowAny], 
            )
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_verification_email(user)
            print('email sent')
            return Response({'status': 'User created successfully, please check your email!'}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], url_path='verify-email', detail=False, permission_classes=[permissions.AllowAny],
            renderer_classes=[renderers.JSONRenderer])
    def verify_email(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = verify_email_verification_token(token)
        if user_id is None:
            return Response({'message': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, id=user_id)
        if user.email_verified == True:
            return Response({'message': 'Email already verified'}, status=status.HTTP_200_OK)

        
        user.email_verified = True
        user.save()

        return Response({'message': 'Email verified successfully!'}, status=status.HTTP_200_OK)
    
    @action(methods=['get'], url_path='account', detail=False, permission_classes=[permissions.AllowAny],
            renderer_classes=[renderers.StaticHTMLRenderer])
    def account(self, request):
        user = request.user
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)

