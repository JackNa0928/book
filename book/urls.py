
from .views import Add_book, Get_books, Get_book_by_ID
from django.urls import path, include

urlpatterns = [
    path('api/books/', Get_books.as_view(), name='books'),
    path('api/book/', Get_book_by_ID.as_view(), name='book_by_id'),
    path('api/add/', Add_book.as_view(), name='add_book'),
]