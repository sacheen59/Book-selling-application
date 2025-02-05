from django import forms
from .models import Category,Book

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['created_at']
        # fields = ['book_name','author']
        # fields = '__all__'