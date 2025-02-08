from django.shortcuts import render
from books.models import Book

# Create your views here.

def homepage(request):
    books = Book.objects.all().order_by('-id')[:8]
    return render(request,'client/homepage.html',{
        'books': books
    })

def bookpage(request):
    books = Book.objects.all().order_by('-created_at')

    return render(request,'client/bookpage.html',{'books':books})

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'client/bookdetail.html',{'book':book})


# add to cart
# delete from cart 
# order
# checout
# myorder 
# marks as deliver(deliver , status deliver)
# payment method 
# logout features
# restriction