from rest_framework import serializers
from books.models import Book
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=("")