from django.shortcuts import render
from django.http import HttpResponse
from .data import list_of_books

# Create your views here.
# function based
# class based views

def index(request):
    return HttpResponse('This is my firstpage.')

def homepage(request):
    list_student = [
        {
            "name":"sachin",
            "course":"python",
        },
        {
            "name": "Zenith",
            "course": "React"
        },
        {
            "name": "Tripti",
            "course": "Graphics"
        },
        {
            "name": "Bandana",
            "course": "Python"
        }
    ]


    context = {
        'data': list_student
    }
    return render(request,"books/index.html",context)


# books = [
#     {
#         "name": 
#         "price"
#         "instock"
#         "description"
#         "author"
#         "published date"
#     }


# ]

def get_all_books(request):
    
    return render(request,"books/allbooks.html",{
        'books': list_of_books
    })

def get_book_by_id(request,book_id):
    data = {}
    for book in list_of_books:
        if book["id"] == int(book_id):
            data["name"] =  book["name"] 
            
    return render(request,"books/book-detail.html",{
       "book": data
    })