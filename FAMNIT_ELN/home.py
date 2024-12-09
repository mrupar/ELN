from django.shortcuts import render
from django.apps import apps

def home(request):
    return render(request, "index.html")
