from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Metric(models.Model):
    visits = models.IntegerField(null=True,blank=True)
    ratio = models.DecimalField(null=True,blank=True,max_digits=2,decimal_places=1)
    def __str__(self):
        return f"{self.visits} visits | ratio: {self.ratio}"

class Tag(models.Model):
    name=models.CharField(max_length=25) 
    def __str__(self):
        return self.name   

class Book(models.Model):
    title=models.CharField( max_length=250)
    author=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Books")
    categories=models.ManyToManyField(Category)
    metrics=models.OneToOneField(Metric,on_delete=models.CASCADE,null=True,blank=True)
    tag=models.ForeignKey(Tag,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



   

