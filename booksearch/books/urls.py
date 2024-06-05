from django.urls import path
from .views import BookList, SearchBooks, RecommendBooksView

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('search/', SearchBooks.as_view(), name='search'),
    path('recommendations/', RecommendBooksView.as_view(), name='recommendations'),
]
