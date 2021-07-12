from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.forms import UserRegisterFrom


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You are now able to log in")
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/profile.html')
