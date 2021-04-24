from rest_framework import serializers
from books.models import Book ,Isbn
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Isbn
        fields=("")