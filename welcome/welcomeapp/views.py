from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<html><body bgcolor=cyan><h1>WELCOME TO HYDERABAD</h1></body></html>")