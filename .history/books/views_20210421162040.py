from django.shortcuts import render
from  django.http import HttpResponse
from .forms import BookForm
# Create your views here.
def index(request):
    return render(request,"books/index.html")
def create(request):
    form=BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"books/create.html",{
        "form":form
    })
