from django .shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from books.models import Book,Isbn
from .serializers import IsbnSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,BasePermission

@api_view("GET")
def index(request):
    books=Book.objects.all()
    serializer=BookSerializer(instance=books , many=True) #multiple object
    return Response(data=serializer.data,status=status.HTTP_200_OK)

