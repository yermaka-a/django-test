from django import http
from django.http import HttpResponse, HttpRequest

def homepage(request: HttpRequest):
    return HttpResponse("Hello world! I'm home")

def about(request: HttpRequest):
    return HttpResponse("My About page.")