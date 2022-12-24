from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .serializers import LogoutSerializer, LoginSerializer, RegisterSerializer
from ..models import User
from rest_framework_simplejwt.tokens import RefreshToken
from item_app.models import ItemList 
# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user =User.objects.get(email = user_data['email'])
        token = RefreshToken.for_user(user).access_token
        return Response(user_data, status = status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):

     serializer_class = LogoutSerializer

     def post(self, request):
         serializer = self.serializer_class(data = request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()

         return Response(status=status.HTTP_204_NO_CONTENT)