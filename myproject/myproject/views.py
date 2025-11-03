from django.http import HttpRequest
from django.shortcuts import render


def homepage(request: HttpRequest):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
