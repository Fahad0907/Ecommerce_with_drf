from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('id', 'username', 'email', 'password','first_name', 'last_name','is_staff')
        extra_kwargs = {'password': {'write_only': True , 'required' : True}}
    def create(self, validated_data,*args, **kwargs):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user