from django.http import HttpResponse, JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .serializers import UserSerializer, RegisterSerializer, AuthCustomTokenSerializer

from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated  

from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            "user": UserSerializer(user, context=self).data,
            "token": AuthToken.objects.create(user)[1]
        })


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

     # Pass to serializer, and create user account 
    def post(self, request, *args, **kwargs):
        data=request.data
        username = data['username']
        if User.objects.filter(email=data['email']):
            return Response({
                "error_message" : "Email has been taken"
            }, status = 400 )
        elif len(username)>28:
            return Response({
                "error_message" : "Username over 28 characters"
            }, status = 400 )
        else:
            serializer = self.get_serializer(data=data)
            print("after get_serializer")
            serializer.is_valid(raise_exception=True)
            print("after serializer.is_valid")
            user = serializer.save()
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            })
