from rest_framework.response import Response
from rest_framework import status
from books.models import Book 
from .serializers import BookSerializer
from rest_framework.decorators import api_view

@api_view("GET")
def index(request):
    pass

