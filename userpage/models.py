from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        # This method returns a string representation of the object
        return f"{self.user.username} - {self.book.name}"