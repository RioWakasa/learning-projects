from django.urls import path
from . import views

urlpatterns = [
  path('book/', views.TestClass.as_view()),
  path('booklist/', views.ListBookView.as_view()),
  path('book/<int:pk>/detail/', views.DetailBookView.as_view()),
  path('book/create/', views.CreateBookView.as_view()),
  path('book/<int:pk>/delete/', views.DeleteBookView.as_view()),
  path('book/<int:pk>/update/', views.UpdateBookView.as_view()),
]