from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('home/',views.homepage),
    path('categories/',views.get_all_categories,name="get-all-categories"),
    path('books/',views.get_all_books,name="get-all-books"),
    path('books/<int:book_id>/',views.get_book_by_id,name="book-detail")
]

