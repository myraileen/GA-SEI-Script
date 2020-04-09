# nostaldja/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('chapters/', views.ChapterList.as_view(), name='chapter_list'),
    path('chapters/<int:pk>', views.ChapterDetail.as_view(), name='chapter_detail'),
    
    path('verses/', views.VerseList.as_view(), name='verse_list'),
    path('verses/<int:pk>', views.VerseDetail.as_view(), name='verse_detail'),
    
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
]