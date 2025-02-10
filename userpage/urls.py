from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('books/',views.bookpage,name='bookpage'),
    path('books/<int:book_id>/',views.book_details,name='book-details'),
    path('addtocart/<int:book_id>/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.cart_page,name='cart'),
    path('cart/<int:cart_id>',views.delete_from_cart,name='delete-from-cart')
]