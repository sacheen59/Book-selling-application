from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .data import list_of_books
from . models import Book,Category
from .forms import CategoryForm,BookForm
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only



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


@login_required
@admin_only
def get_all_categories(request):
    all_categories = Category.objects.all()
    return render(request,"books/category/allcategories.html",{
        'categories': all_categories
    })

@login_required
@admin_only
# Define a function called post_category that takes in a request as a parameter
def post_category(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Create a form object using the CategoryForm class and the POST data from the request
        form = CategoryForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Add a success message to the messages framework
            messages.add_message(request,messages.SUCCESS,"Category added successfully")
            # Redirect the user to the categories page
            return redirect("/books/categories/")
        else:
            # Add an error message to the messages framework
            messages.add_message(request,messages.ERROR,"Failed to add category")
            # Render the postcategory.html template and pass in the form object
            return render(request,"books/category/postcategory.html",{'form': form})
    
    # Render the postcategory.html template and pass in the CategoryForm class
    return render(request,"books/category/postcategory.html",{
        'form': CategoryForm
    })

@login_required
@admin_only
# Define a function to delete a category
def delete_category(request,category_id):
    # Get the category object from the database using the category_id
    category = Category.objects.get(id=category_id)
    # Delete the category object
    category.delete()
    # Add a success message to the request
    messages.add_message(request,messages.SUCCESS,"Category deleted successfully")
    # Redirect the user to the categories page
    return redirect("/books/categories/")


@login_required
@admin_only
# updage category 
# Define a function to update a category
def update_category(request,category_id):
    # Get the category object from the database using the category_id
    category = Category.objects.get(id=category_id)
    # Check if the request method is POST
    if request.method == "POST":
        # Create a form instance using the POST data and the category object
        form = CategoryForm(request.POST,instance=category)
        # Check if the form is valid
        if form.is_valid():
            # Save the form
            form.save()
            # Add a success message
            messages.add_message(request,messages.SUCCESS,"Category updated successfully")
            # Redirect to the categories page
            return redirect("/books/categories/")
        else:
            # Add an error message
            messages.add_message(request,messages.ERROR,"Failed to update category")
            # Render the postcategory.html template with the form
            return render(request,"books/category/updatecategory.html",{'form': form})
    return render(request,"books/category/updatecategory.html",{

        'form': CategoryForm(instance=category)
    }
)

@login_required
@admin_only
# get all books 
def get_all_books(request):
    all_books = Book.objects.all()
    return render(request,"books/book/allbooks.html",{
        'books': all_books
    })

@login_required
@admin_only
# post book
def post_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Book Added Successfully')
            return redirect('/books/') #http://localhost:8000/books
        else:
            messages.add_message(request,messages.ERROR,'Failed to Add book')
            return render(request,'books/book/postbook.html',{'form': form})
        
    return render(request,"books/book/postbook.html",{
        'form': BookForm
    }
    )

@login_required
@admin_only
# delete book
def delete_book(request,book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    messages.add_message(request,messages.SUCCESS,'Book Deleted Successfully')
    return redirect('/books/')

@login_required
@admin_only
# update book
# Define a function to update a book
def update_book(request,book_id):
    # Get the book object from the database using the book_id
    book = Book.objects.get(pk=book_id)
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the POST data and the book object
        form = BookForm(request.POST,instance=book)
        # Check if the form is valid
        if form.is_valid():
            # Save the form
            form.save()
            # Add a success message
            messages.add_message(request,messages.SUCCESS,'Book Updated Successfully')
            # Redirect to the books page
            return redirect('/books/')
        else:
            # Add an error message
            messages.add_message(request,messages.ERROR,'Failed to Update book')
            # Render the updatebook.html template with the form
            return render(request,'books/book/updatebook.html',{'form': form})
    # Render the updatebook.html template with the book form
    return render(request,'books/book/updatebook.html',{
        'form': BookForm(instance=book)
    })



@login_required
@admin_only
# admin dashboard 
def admin_dashboard(request):
    return render(request,"books/dashboard/dashboard.html")
