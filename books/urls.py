from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('home/',views.homepage),
    path('allbooks/',views.get_all_books,name="get-all-books"),
    path('bookdetail/<int:book_id>/',views.get_book_by_id,name="book-detail")
]

