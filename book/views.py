from django.http import HttpResponse, JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Books

from .serializers import BookAPI

from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated

from knox.auth import TokenAuthentication
from knox.models import AuthToken

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class Add_book(generics.GenericAPIView):
    serializer_class = BookAPI
    model = Books
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = BookAPI(data=data)
        if serializer.is_valid():
            book = Books.objects.create(name=data["name"])
            book.save()
            return JsonResponse(data) 
        else:
            return Response(serializer.errors, status = 400)

class Get_books(generics.GenericAPIView):

    
    def get(self, request, *args, **kwargs):
        books = Books.objects.all()
        output = []
        for book in books:
            output.append({
                    "id":book.id,
                    "name":book.name,
                })
        return Response(output)



class Get_book_by_ID(generics.GenericAPIView):


    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        book = Books.objects.get(id=data["id"])
        print(book.name)
        return JsonResponse({
            "id": book.id,
            "name": book.name
        })

