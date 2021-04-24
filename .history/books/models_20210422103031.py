from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

class Metric(models.Model):
    visits=models.IntegerField(null=True,blank=True)
    ratio=models.DecimalField(null=True,blank=True,max_digits=2,decimal_places=1)


class Book(models.Model):
    title=models.CharField( max_length=250)
    author=models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="books")
    categories=models.ManyToManyField(Category)
    metrics=models.OneToOneField(Metric,on_delete=models.CASCADE,null=True,blank=true)
    
    def __str__(self):
        return self.title


   

