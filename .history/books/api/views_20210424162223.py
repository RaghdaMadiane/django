from rest_framework.response import Response
from rest_framework import status
from books.models import Book ,Isbn
from .serializers import BookSerializer
from rest_framework.decorators import api_view , permission_classes
from rest_framework import generics
from rest_framework import viewsets


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="viewers").exists()

@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User has been registered successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

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
           "success":True,
           "message":"Book has been created successfully " 
        },status=status.HTTP_201_CREATED)
    return Response(data={
           "success":False,
           "errors":serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

