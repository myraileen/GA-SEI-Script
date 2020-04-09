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
        fields = ('version', 'book_num', 'book', 'description', 'image_url', 'chapters',)

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
        fields = ('book', 'chapter_num', 'chapter', 'description', 'image_url', 'verses',)

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
        fields = ('verse_num', 'verse', 'image_url', 'chapter',)
