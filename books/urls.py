from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('home/',views.homepage),

    path('categories/',views.get_all_categories,name="get-all-categories"),
    path('addcategory/',views.post_category,name="post-category"),
    path('deletecategory/<int:category_id>/',views.delete_category,name="delete-category"),
    path('updatecategory/<int:category_id>/',views.update_category,name="update-category"),

    path('allbooks',views.get_all_books,name="get-all-books"),
    path('addbook/',views.post_book,name="post-book"),
    path('deletebook/<int:book_id>/',views.delete_book,name="delete-book"),
    path('updatebook/<int:book_id>/',views.update_book,name="update-book"),

    # dasboard path 
    path('dashboard/',views.admin_dashboard,name="admin-dashboard"),
    path('allorders/',views.all_orders,name="all-orders"),
    path('customers/',views.customers,name="customers"),

]
