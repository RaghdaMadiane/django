from rest_framework.response import Response
from rest_framework import status
def index(request):
    book=Book.objects.all()
    return Response

