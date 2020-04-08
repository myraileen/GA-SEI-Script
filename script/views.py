from django.shortcuts import render, redirect

from .models import Chapter, Verse
from .forms import ChapterForm

# Create your views here.
def chapter_list(request):
    chapters = Chapter.objects.order_by('chapter_num') 
    return render(request, 'script/chapter_list.html', {'chapters': chapters})

def chapter_detail(request, pk):
    chapter = Chapter.objects.get(id=pk)
    return render(request, 'script/chapter_detail.html', {'chapter': chapter})

def chapter_create(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save()
            return redirect('chapter_detail', pk=chapter.pk)
    else:
        form = ChapterForm()
    return render(request, 'nostaldja/chapter_form.html', {'form': form})

def chapter_edit(request, pk):
    chapter = Chapter.objects.get(pk=pk)
    if request.method == "POST":
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            chapter = form.save()
            return redirect('chapter_detail', pk=chapter.pk)
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'nostaldja/chapter_form.html', {'form': form})

def chapter_delete(request,pk):
    Chapter.objects.get(id=pk).delete()
    return redirect('chapter_list')