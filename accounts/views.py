from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        if user := authenticate(username=username, password=password):
            login(request, user)
            return redirect("/books")

    return render(request, "registration/register.html", {"form": form})
