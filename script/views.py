from django.shortcuts import render, redirect

from .models import Chapter, Verse

# Create your views here.
def chapter_list(request):
    chapters = Chapter.objects.order_by('chapter_num') 
    return render(request, 'script/chapter_list.html', {'chapters': chapters})
