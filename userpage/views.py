from django.shortcuts import render,redirect
from django.http import HttpResponse
from books.models import Book
from django.contrib.auth.decorators import login_required
from .models import Cart,Order
from django.contrib import messages
from accounts.auth import user_only
from .forms import OrderFrom
from django.contrib import messages
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

@login_required
@user_only
def user_order(request,cart_id,book_id):
    user = request.user
    book = Book.objects.get(id = book_id)
    cart = Cart.objects.get(id = cart_id)
    if request.method == 'POST':
        form = OrderFrom(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            quantity = data['quantity']
            price = book.price
            total_price = int(quantity) * int(price)
            payment_method = data['payment_method']
            contact_no = data['contact_no']
            address = data['address']

            order = Order.objects.create(
                book = book,
                user = user,
                quantity = quantity,
                total_price = total_price,
                payment_method = payment_method,
                contact_no = contact_no,
                address = address
            )

            if order.payment_method == 'Cash on Delivery':
                cart.delete()
                messages.add_message(request,messages.SUCCESS,'Order placed successfully')
                return redirect('/myorders')
        else:
            messages.add_message(request,messages.ERROR,'Order Failed')
            return render(request,'client/orderform.html',{'form':form})
    return render(request,'client/orderform.html',{'form':OrderFrom})


@login_required
@user_only
def show_myorder(request):
    user = request.user
    orders = Order.objects.filter(user = user)
    return render(request,'client/myorder.html',{'orders':orders})


@login_required
@user_only
def mark_as_deliver(request,order_id):
    order = Order.objects.get(id = order_id)
    order.status = 'Delivered...'
    order.save()
    messages.add_message(request,messages.SUCCESS,'Order marked as delivered')
    return redirect('/myorders')
