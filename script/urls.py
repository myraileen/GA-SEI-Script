# nostaldja/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chapter_list, name='chapter_list'),
    path('chapters/<int:pk>/', views.chapter_detail, name='chapter_detail'),
    path('chapters/new', views.chapter_create, name='chapter_create'),
    path('chapters/<int:pk>/edit', views.chapter_edit, name='chapter_edit'),
    path('chapters/<int:pk>/delete', views.chapter_delete, name='chapter_delete'),
    path('verses/', views.verse_list, name='verse_list'),
    path('verses/<int:pk>/', views.verse_detail, name='verse_detail'),
    path('verses/new', views.verse_create, name='verse_create'),
    path('verses/<int:pk>/edit', views.verse_edit, name='verse_edit'),
    path('verses/<int:pk>/delete', views.verse_delete, name='verse_delete'),
]