from rest_framework import serializers
from .models import Author, Genre, Book, BookCopy, BookLending

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class BookCopySerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = BookCopy
        fields = '__all__'

class BookLendingSerializer(serializers.ModelSerializer):
    book_copy = BookCopySerializer(read_only=True)

    class Meta:
        model = BookLending
        fields = '__all__'