from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book

class TestClass(TemplateView):
  template_name = 'test.html'

class ListBookView(ListView):
  template_name = 'book/book/list.html'
  model = Book

class DetailBookView(DetailView):
  template_name = 'book/book_detail.html'
  model = Book

class CreateBookView(CreateView):
  template_name = 'book/book_create.html'
  model = Book

class DeleteBookView(DeleteView):
  template_name = 'book/book_confirm.html'
  model = Book

class UpdateBookView(UpdateView):
  template_name = 'book/book_update.html'
  model = Book