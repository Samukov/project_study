from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'photo', 'age', 'gender', 'phone_number',
                  'region']
        read_only_fields = ['id', 'username', 'email', 'photo']  # Поля, которые только для чтения


class UserRegisterSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'},
                                      label=_("Password"))  # Пароль
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'},
                                      label=_("Password confirmation"))  # Подтверждение пароля

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'photo', 'age', 'gender',
                  'phone_number', 'region']

    def validate(self, attrs):

        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(_("The two passwords do not match."))  # Проверка на совпадение паролей
        return attrs

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            photo=validated_data['photo'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            phone_number=validated_data['phone_number'],
            region=validated_data['region']
        )
        return user


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):

        user = User.objects.filter(username=attrs.get("username")).first()
        if user and user.check_password(attrs.get("password")):
            return user
        raise serializers.ValidationError(_("Incorrect username or password."))


class UserLogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    def validate(self, attrs):

        try:
            RefreshToken(attrs['refresh']).blacklist()
        except Exception:
            raise serializers.ValidationError(_("Invalid refresh token."))
        return attrs


class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'photo', 'age', 'gender', 'phone_number', 'region']
