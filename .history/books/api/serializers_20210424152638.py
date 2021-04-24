from rest_framework import serializers
from books.models import Isbn
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Isbn
        fields='__all__'