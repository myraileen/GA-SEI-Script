from rest_framework import serializers
from .models import Chapter, Verse, Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    chapters = serializers.HyperlinkedRelatedField(
        view_name='chapter_detail',
        many=True,
        read_only=True
    )

    book_url = serializers.ModelSerializer.serializer_url_field(
        view_name='book_detail'
    )

    class Meta:
        model = Book
        fields = ('id', 'book_url', 'photo_url', 'nationality', 'name', 'chapters',)

class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    verses = serializers.HyperlinkedRelatedField(
        view_name='verse_detail',
        many=True,
        read_only=True
    )

    chapter_url = serializers.ModelSerializer.serializer_url_field(
        view_name='chapter_detail'
    )

    class Meta:
        model = Chapter
        fields = ('id', 'chapter_url', 'photo_url', 'nationality', 'name', 'verses',)

class VerseSerializer(serializers.HyperlinkedModelSerializer):
    chapter = serializers.HyperlinkedRelatedField(
        view_name='chapter_detail',
        read_only=True
    )

    verse_url = serializers.ModelSerializer.serializer_url_field(
        view_name='verse_detail'
    )

    class Meta:
        model = Verse
        fields = ('id', 'verse_url', 'preview_url', 'album', 'title', 'chapter',)




    