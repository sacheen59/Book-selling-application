from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('home/',views.homepage),
    path('categories/',views.get_all_categories,name="get-all-categories"),
    path('addcategory/',views.post_category,name="post-category"),
    path('deletecategory/<int:category_id>/',views.delete_category,name="delete-category"),
    path('updatecategory/<int:category_id>/',views.update_category,name="update-category"),
    path('',views.get_all_books,name="get-all-books"),
]
