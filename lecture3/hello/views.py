from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requset):
    return HttpResponse("Hello, world!")

def greeting(request):
    return HttpResponse("Hello, Gaman!")