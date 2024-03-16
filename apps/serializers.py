from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = 'username', 'email', 'password', 'confirm_password'

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError('Bu email bazada bor')
        return value

    def validate(self, data):
        confirm_password = data.pop('confirm_password')
        if confirm_password and confirm_password == data['password']:
            data['password'] = make_password(data['password'])
            data['is_active'] = False
            return data
        raise ValidationError("Parol mos emas")
