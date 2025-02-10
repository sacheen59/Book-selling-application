from django.shortcuts import render,redirect
from django.http import HttpResponse
from books.models import Book
from django.contrib.auth.decorators import login_required
from .models import Cart
from django.contrib import messages
from accounts.auth import user_only
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
@login_required
@user_only
def add_to_cart(request,book_id):
    user = request.user
    book = Book.objects.get(id = book_id)

    check_book_presence = Cart.objects.filter(user = user,book = book)

    if check_book_presence:
        messages.add_message(request,messages.ERROR,'This book is already in your cart')
        return redirect('/books')
    else:
        cart = Cart.objects.create(user = user,book = book)
        if cart:
            messages.add_message(request,messages.SUCCESS,'Book added to cart successfully')
            return redirect('/cart')
        else:
            messages.add_message(request,messages.ERROR,'Failed to add book to cart')
            return redirect('/books')

@login_required
@user_only       
# Define a function called cart_page that takes in a request as a parameter
def cart_page(request):
    # Get the user from the request
    user = request.user
    # Get the cart from the database that is associated with the user
    carts = Cart.objects.filter(user = user)
    # Render the cart.html template and return it
    return render(request,'client/cart.html',{'carts':carts})
        


# delete from cart 
@login_required
@user_only
def delete_from_cart(request, cart_id):
    user = request.user
    cart = Cart.objects.filter(user = user ,id = cart_id)
    cart.delete()
    messages.add_message(request,messages.SUCCESS,'Book removed from cart successfully')
    return redirect('/cart')

# order
# checout
# myorder 
# marks as deliver(deliver , status deliver)
# payment method 
# logout features
