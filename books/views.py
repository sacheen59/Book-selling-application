from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .data import list_of_books
from . models import Book,Category
from .forms import CategoryForm



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
    all_books = Book.objects.all()
    return render(request,"books/allbooks.html",{
        'books': all_books
    })

def get_all_categories(request):
    all_categories = Category.objects.all()
    return render(request,"books/allcategories.html",{
        'categories': all_categories
    })

def post_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Category added successfully")
            return redirect("/books/categories/")
        else:
            messages.add_message(request,messages.ERROR,"Failed to add category")
            return render(request,"books/postcategory.html",{'form': form})
    
    return render(request,"books/postcategory.html",{
        'form': CategoryForm
    })

def delete_category(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,"Category deleted successfully")
    return redirect("/books/categories/")


def get_book_by_id(request,book_id):
    data = {

    }
    for book in list_of_books:
        if book["id"] == int(book_id):
            data["id"] = int(book_id)
            data["name"] =  book["name"]

    print(data)
            
    return render(request,"books/book-detail.html",{
       "book": data
    })


class A:
    pass

obj = A()