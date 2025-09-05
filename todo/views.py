from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return HttpResponse("<H1>Hello, world<H1>")


def books(request):
    my_books = {1:"Django", 2:"Python", 3:"JavaScript"}
    return HttpResponse(json.dumps(my_books),
content_type = "application/json") 