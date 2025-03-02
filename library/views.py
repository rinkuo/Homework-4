from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Author, Genre, Book, BookCopy, BookLending
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer, BookCopySerializer, BookLendingSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = CustomPageNumberPagination

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = CustomPageNumberPagination

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCopyListCreateView(generics.ListCreateAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    pagination_class = CustomPageNumberPagination

class BookCopyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

class BookLendingListCreateView(generics.ListCreateAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer
    pagination_class = CustomPageNumberPagination

class BookLendingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer