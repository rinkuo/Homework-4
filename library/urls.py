from django.urls import path
from .views import (
    AuthorListCreateView, AuthorRetrieveUpdateDestroyView,
    GenreListCreateView, GenreRetrieveUpdateDestroyView,
    BookListCreateView, BookRetrieveUpdateDestroyView,
    BookCopyListCreateView, BookCopyRetrieveUpdateDestroyView,
    BookLendingListCreateView, BookLendingRetrieveUpdateDestroyView
)

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-retrieve-update-destroy'),
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-retrieve-update-destroy'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    path('copies/', BookCopyListCreateView.as_view(), name='bookcopy-list-create'),
    path('copies/<int:pk>/', BookCopyRetrieveUpdateDestroyView.as_view(), name='bookcopy-retrieve-update-destroy'),
    path('lendings/', BookLendingListCreateView.as_view(), name='booklending-list-create'),
    path('lendings/<int:pk>/', BookLendingRetrieveUpdateDestroyView.as_view(), name='booklending-retrieve-update-destroy'),
]