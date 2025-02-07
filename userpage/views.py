from django.shortcuts import render
from books.models import Book

# Create your views here.

def homepage(request):
    books = Book.objects.all().order_by('-id')[:4]
    return render(request,'client/homepage.html',{
        'books': books
    })

def bookpage(request):
    return render(request,'client/bookpage.html')