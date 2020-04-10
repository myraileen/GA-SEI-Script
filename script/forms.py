# tunr/forms.py
from django import forms
from .models import Chapter, Verse, Book

class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ('book','chapter_num','chapter','description','image_url')

class VerseForm(forms.ModelForm):

    class Meta:
        model = Verse
        fields = ('chapter','verse_num','verse','image_url')

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('version','book_num','book','description','image_url')

class ConfirmDelete(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ('book','chapter_num','chapter','description','image_url')
