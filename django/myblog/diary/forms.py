from ast import keyword
from dataclasses import field
from socket import fromshare
from django import forms
from .models import Diary

class SerchForm(forms.Form):
  keyword = forms.CharField(label='検索', max_length=50)

class DiaryForm(forms.ModelForm):
  class Meta:
    model = Diary
    fields = ('topic')