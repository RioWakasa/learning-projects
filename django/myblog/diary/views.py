from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Diary

def index(request):
    diaries = Diary.objects.all()
    context = {
        'message': 'Hello my diary',
        'diaries': diaries,
    }
    return render(request, 'diary/index.html', context)

def create(request):
    diaries = Diary(topic="It's a sunny day today.")
    diaries.save()
    
    diaries = Diary.objects.all()
    context = {
        'message': 'CREATE diary',
        'diaries': diaries,
    }

    return render(request, 'diary/index.html', context)