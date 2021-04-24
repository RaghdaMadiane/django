from django.shortcuts import render
from  django.http import HttpResponse
from .forms import BookForm
# Create your views here.
def index(request):
    return render(request,"books/index.html")
def create(request):
    book=BookForm(request.Book or None)