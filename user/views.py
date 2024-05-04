from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    """Представление для регистрации нового пользователя."""

    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny] # Разрешить доступ без аутентификации


class UserLoginView(generics.GenericAPIView):
    """Представление для входа пользователя."""

    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny] # Разрешить доступ без аутентификации

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class UserLogoutView(generics.GenericAPIView):
    """Представление для выхода пользователя."""

    serializer_class = UserLogoutSerializer
    permission_classes = [permissions.IsAuthenticated] # Только для аутентифицированных пользователей

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """Представление для просмотра и обновления данных профиля пользователя."""

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] # Только для аутентифицированных пользователей

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(generics.UpdateAPIView):
    """Представление для обновления данных профиля пользователя."""

    serializer_class = UserProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только для аутентифицированных пользователей

    def get_object(self):
        return self.request.user
