from rest_framework.response import Response
from rest_framework import status
from books.models import Book ,Isbn
from .serializers import BookSerializer
from rest_framework.decorators import api_view

@api_view(["GET"])
def index(request):
    books=Isbn.objects.all()
    serializer=BookSerializer(instance=books , many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)
@api_view(["POST"])
def create(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
           "success":True
           "message":"Book has been created successfully " 
        },status=status.HTTP_201_CREATED)
    return Response(data={
           "success":False
           "errors":serializer.errors
        },status=status.HTTP_201_CREATED)

