from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based
# class based views

def index(request):
    return HttpResponse('This is my firstpage.')

def homepage(request):
    return render(request,"books/index.html")

