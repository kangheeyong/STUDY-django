from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import UserRegisterFrom


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Acount created for {username}!")
            return redirect('blog-home')
    else:
        form = UserRegisterFrom()

    return render(request, "users/register.html", {"form": form})