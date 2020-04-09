from .models import Chapter, Verse, Book
from rest_framework import generics
from .serializers import ChapterSerializer, VerseSerializer, BookSerializer

class ChapterList(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class VerseList(generics.ListCreateAPIView):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer

class VerseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer