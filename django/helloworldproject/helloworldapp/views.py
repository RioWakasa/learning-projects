from django.shortcuts import render
from django.http import HttpResponse

def helloworldfunc(reqest):
  return HttpResponse('hello world')
