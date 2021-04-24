from django.shortcuts import redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid:
        form.save()
        username=form.cleaned_data.get("username")
        username=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect("index")
    return render(request, "registration/signuo.html",{
        'form':form
    })


