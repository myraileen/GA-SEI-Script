# nostaldja/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chapter_list, name='chapter_list'),
    path('chapters/<int:pk>/', views.chapter_detail, name='chapter_detail'),
    path('chapters/new', views.chapter_create, name='chapter_create'),
    path('chapters/<int:pk>/edit', views.chapter_edit, name='chapter_edit'),
    path('chapters/<int:pk>/delete', views.chapter_delete, name='chapter_delete'),
]