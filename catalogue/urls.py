from django.urls import path

from catalogue import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail')

]