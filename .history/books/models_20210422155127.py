from django.contrib.auth.models import User
from django.db import models
import uuid

class Tag(models.Model):
    name = models.CharField(max_length=25)

class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    


class Isbn(models.Model):
    book_isbn = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True,max_length=13, editable=False, help_text="Unique ID for this particular book across whole library")
    

class Book(models.Model):
    title=models.CharField( max_length=250)
    author=models.CharField(max_length=100)
    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name="Book")
    categories=models.ManyToManyField(Category)
    isbn= models.UUIDField(Isbn,primary_key=True, default=uuid.uuid4, editable=False ,max_length=13)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



   

