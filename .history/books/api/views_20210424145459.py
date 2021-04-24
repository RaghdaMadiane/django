from rest_framework.response import Response
from rest_framework import status
from books.model import Book
from .serializers import BookSerializer
def index(request):
    books=Book.objects.all()
    serializer=BookSerializer(instance=books , many=True) #multiple object
    return Response(data=serializer.data,status=status.HTTP_200_OK)

