from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post


def home(request: HttpRequest) -> HttpResponse:
    context = {
        "posts": Post.objects.order_by("-date_posted").all()
    }
    return render(request, "blog/home.html", context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/about.html", {"title": "About"})
