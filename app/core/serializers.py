from rest_framework.serializers import ModelSerializer , Serializer
import rest_framework.serializers as serializers
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth import authenticate

class UserSerializer (ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id","email","password","username"]
        extra_kwargs={'password':{'write_only':True}}
        
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)        
    
    
class TokenAuthSerializer (Serializer):
    email = serializers.CharField(max_length=25)
    password =  serializers.CharField(max_length=5,write_only=True)   
    
    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        
        if email is None:
            raise serializers.ValidationError('email is required for login')
        if password is None:
            raise serializers.ValidationError('password is required for login')
        
        user = authenticate(email=email,password=password)
        
        if not user:
            raise serializers.ValidationError("invalis user credentials")
        
        return user