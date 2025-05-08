from rest_framework import serializers
from .models import User 


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User 
        fields = ['id','email', 'name', 'password']


    def create(self, validate_data):
        return User.objects.create_user(**validate_data)