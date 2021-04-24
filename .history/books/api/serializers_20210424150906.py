from django .shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from books.models import Book,Isbn
from .serializers import IsbnSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,BasePermission
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Isbn
        fields=("book_title","author")