from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.models import Token


class AuthView(APIView):
    @staticmethod
    def post(request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not (email and password):
            return Response({'error': 'Provide email and password'}, status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(User, email=email)
        if not user.check_password(password):
            return Response({'error': 'Invalid email or password'}, status.HTTP_400_BAD_REQUEST)
        return Response({'token': Token.objects.create(user=user).id}, status.HTTP_200_OK)


class RegisterView(APIView):
    @staticmethod
    def post(request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not (email and password):
            return Response({'error': 'Provide email and password'}, status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'error': 'User with this email already exists'}, status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(email=email, password=password)
        return Response({'token': Token.objects.create(user=user).id}, status.HTTP_201_CREATED)


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request, **kwargs):
        try:
            token_id = request.headers.get('Authorization').split('Bearer')[1].strip()
            user = Token.objects.get(id=token_id).user
            return user, None
        except (IndexError, ValidationError, Token.DoesNotExist):
            return None
