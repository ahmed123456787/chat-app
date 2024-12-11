from django.shortcuts import render
from .serializers import * 
from .views import *
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class UserCreateView (CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser
    
    
class RegisterView (CreateAPIView): 
    serializer_class = TokenAuthSerializer
    
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        # Check if both email and password are provided
        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user using Django's authenticate method
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Generate JWT tokens if authentication is successful
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Prepare the response with tokens and user data
            response_data = {
                "refresh": refresh_token,
                "access": access_token,
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Return error if authentication fails
            return Response(
                {"error": "Invalid credentials. Please check your email and password."},
                status=status.HTTP_401_UNAUTHORIZED
            )