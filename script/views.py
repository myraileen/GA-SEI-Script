from django.shortcuts import render, redirect

from .models import Chapter

# Create your views here.
def chapter_list(request):
    decades = Decade.objects.order_by('start_year') 
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})
