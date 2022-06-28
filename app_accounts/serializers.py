from rest_framework import serializers
from .models import NewUser


class NewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = '__all__'
