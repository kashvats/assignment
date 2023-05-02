from rest_framework import serializers
# from . import models
from .models import User,product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = ["item_name","item_image","description","price","deleted","owner","id"]



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=40, min_length=4)
    password = serializers.CharField(max_length=25, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', "roles","password"]

    def validate(self, args):
        email = args.get('email', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exist'})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

