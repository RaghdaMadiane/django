from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField( max_length=250)
    author=models.models.CharField(max_length=2050)