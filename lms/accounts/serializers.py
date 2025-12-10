from rest_framework import serializers
from .models import Account


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Account
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name',
            'phone_number', 'address', 'password'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Account.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['password']
