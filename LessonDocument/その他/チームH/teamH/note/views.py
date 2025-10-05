from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Subject, Document

def index(request):
  subjects = Subject.objects.all()
  context = {
    'subjects': subjects,
  }
  return render(request, 'note/index.html', context)

def subject(request, id):
  subject = get_object_or_404(Subject, pk=id)
  documents = Document.objects.all()
  context = {
    'id': str(id),
    'subject': subject,
    'documents': documents,
  }
  return render(request, 'note/subject.html', context)

def detail(request,id):
  
  context = {
  }
  return render(request, 'note/detail.html', context)