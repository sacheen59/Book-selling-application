from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('books/',views.bookpage,name='bookpage'),
    path('books/<int:book_id>/',views.book_details,name='book-details'),
    path('addtocart/<int:book_id>/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.cart_page,name='cart'),
    path('cart/<int:cart_id>',views.delete_from_cart,name='delete-from-cart'),
    path('order/<int:cart_id>/<int:book_id>/',views.user_order,name='user-order'),
    path('myorders/',views.show_myorder,name='myorders'),
    path('markasdeliver/<int:order_id>/',views.mark_as_deliver,name='mark-as-deliver'),
]