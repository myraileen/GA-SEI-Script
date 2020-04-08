# tunr/forms.py
from django import forms
from .models import Chapter, Verse

class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ('book','chapter_num','chapter','description','image_url')

class VerseForm(forms.ModelForm):

    class Meta:
        model = Verse
        fields = ('chapter','verse_num','verse','image_url')
