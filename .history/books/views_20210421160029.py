from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"books/index.html")
def create(request):
    pass=BookForm(request.Book or None)