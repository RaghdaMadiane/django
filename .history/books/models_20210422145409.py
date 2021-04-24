from django.contrib.auth.models import User
from django.db import models
from isbn_field import ISBNField


class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    


# class Isbn(models.Model):
#     book_isbn = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False, help_text="Unique ID for this particular book across whole library")
#     def __str__(self):
#         return self.book_isbn  

class Book(models.Model):
    title=models.CharField( max_length=250)
    author=models.CharField(max_length=100)
    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name="Book")
    categories=models.ManyToManyField(Category)
    isbn = ISBNField()
    

    def __str__(self):
        return self.title



   
