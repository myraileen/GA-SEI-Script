from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Chapter, Verse, Book
from .forms import ChapterForm, VerseForm, BookForm

# Chapter Views
@login_required
def chapter_list(request):
    chapters = Chapter.objects.order_by('chapter_num') 
    return render(request, 'script/chapter_list.html', {'chapters': chapters})

@login_required
def chapter_detail(request, pk):
    chapter = Chapter.objects.get(id=pk)
    return render(request, 'script/chapter_detail.html', {'chapter': chapter})

@login_required
def chapter_create(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save()
            return redirect('chapter_detail', pk=chapter.pk)
    else:
        form = ChapterForm()
    return render(request, 'script/chapter_form.html', {'form': form})

@login_required
def chapter_edit(request, pk):
    chapter = Chapter.objects.get(pk=pk)
    if request.method == "POST":
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            chapter = form.save()
            return redirect('chapter_detail', pk=chapter.pk)
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'script/chapter_form.html', {'form': form})

@login_required
def chapter_delete(request,pk):
    Chapter.objects.get(id=pk).delete()
    return redirect('chapter_list')

# Verse Views
@login_required
def verse_list(request):
    verses = Verse.objects.order_by('chapter','verse_num') 
    return render(request, 'script/verse_list.html', {'verses': verses})

@login_required
def verse_detail(request, pk):
    verse = Verse.objects.get(id=pk)
    return render(request, 'script/verse_detail.html', {'verse': verse})

@login_required
def verse_create(request):
    if request.method == 'POST':
        form = VerseForm(request.POST)
        if form.is_valid():
            verse = form.save()
            return redirect('verse_detail', pk=verse.pk)
    else:
        form = VerseForm()
    return render(request, 'script/verse_form.html', {'form': form})

@login_required
def verse_edit(request, pk):
    verse = Verse.objects.get(pk=pk)
    if request.method == "POST":
        form = VerseForm(request.POST, instance=verse)
        if form.is_valid():
            verse = form.save()
            return redirect('verse_detail', pk=verse.pk)
    else:
        form = VerseForm(instance=verse)
    return render(request, 'script/verse_form.html', {'form': form})

@login_required
def verse_delete(request,pk):
    Verse.objects.get(id=pk).delete()
    return redirect('verse_list')

# Book Views
@login_required
def book_list(request):
    books = Book.objects.order_by('book_num') 
    return render(request, 'script/book_list.html', {'books': books})

@login_required
def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'script/book_detail.html', {'book': book})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'script/book_form.html', {'form': form})

@login_required
def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'script/book_form.html', {'form': form})

@login_required
def book_delete(request,pk):
    Book.objects.get(id=pk).delete()
    return redirect('book_list')