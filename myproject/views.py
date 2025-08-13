from django import http
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def homepage(request: HttpRequest):
    return render(request, "home.html")
    
def about(request: HttpRequest):
    return render(request, "about.html")