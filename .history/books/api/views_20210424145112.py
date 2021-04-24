from rest_framework.response import Response
from rest_framework import status
from books.model import Book
def index(request):
    book=Book.objects.all()
    return Response

