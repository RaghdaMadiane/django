from django.db import models


class book(models.Model):
    title=models.CharField( max_length=250)
    author=models.models.CharField(max_length=2050)