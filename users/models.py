from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
# Create your models here.
from rest_framework.serializers import ModelSerializer


class User(AbstractUser):
    middle_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)


class UserSerializer(ModelSerializer):
    first_name = models.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'middle_name', 'phone_number', 'address')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('email',)
            )
        ]


class UserCurrentSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'middle_name', 'phone_number', 'address')
        extra_kwargs = {
            'phone_number': {"required": False},
            'middle_name': {"required": False},
        }

