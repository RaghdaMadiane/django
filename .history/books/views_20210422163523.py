from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book

def index(request):
    books =Book.objects.all()
    return render(request,"books/index.html",{
        "books":books
    })
def create(request):
    form=BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"books/create.html",{
        "form" : form
    })
def edit(request,isbn):
    book=Book.objects.get(id=isbn)
    form =BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request,"books/edit.html",{
        "form" : form,
        "book" : book
    })
def delete(request, isbn): 
    book=Book.objects.get(id=isbn)  
    book.delete()  
    return redirect("index")
