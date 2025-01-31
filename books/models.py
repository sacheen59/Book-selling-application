from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category_name}"


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    instock = models.BooleanField(default=True)
    imageUrl = models.CharField(max_length=300)
    description = models.TextField()
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.author})"


