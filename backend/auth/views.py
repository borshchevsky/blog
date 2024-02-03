from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.authentication import BaseAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from auth.models import Token, User
from auth.serializers import UserSerializer
from main.utils import extract_token


class AuthView(APIView):
    @staticmethod
    def post(request):
        token_id = extract_token(request)
        if token_id:
            if Token.objects.filter(id=token_id).exists():
                return Response({'detail': 'ok'}, status.HTTP_200_OK)
        email = request.data.get('email')
        password = request.data.get('password')
        if not (email and password):
            return Response({'error': 'Provide email and password'}, status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(User, email=email)
        if not user.check_password(password):
            return Response({'error': 'Invalid email or password'}, status.HTTP_400_BAD_REQUEST)
        token = Token.objects.create(user=user).id
        response = Response({'token': token}, status.HTTP_200_OK)
        response.set_cookie('Authorization', f'Bearer {token}')
        return response


class RegisterView(APIView):
    @staticmethod
    def post(request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not (email and password):
            return Response({'error': 'Provide email and password'}, status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'error': 'User with this email already exists'}, status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=email, email=email, password=password)
        token = Token.objects.create(user=user).id
        response = Response({'token': token}, status.HTTP_201_CREATED)
        response.set_cookie('Authorization', f'Bearer {token}')
        return response


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request, **kwargs):
        try:
            token_id = extract_token(request)
            user = Token.objects.get(id=token_id).user
            return user, None
        except Token.DoesNotExist:
            return None


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        token = extract_token(self.request)
        return get_object_or_404(Token, id=token).user

    @action(detail=False, methods=['get'])
    def get_current_user(self, request):
        return self.retrieve(request)
