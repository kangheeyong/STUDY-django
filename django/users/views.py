from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.forms import UserRegisterFrom, UserUpdateForm, ProfileUpdateForm


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
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
