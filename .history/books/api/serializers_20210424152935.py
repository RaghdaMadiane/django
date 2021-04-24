from rest_framework import serializers
from books.models import Book , Isbn
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=("book_title","author")