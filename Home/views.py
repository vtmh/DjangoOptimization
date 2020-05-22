from django.shortcuts import render

# Create your views here.

def homepage(request):

    return render(request, 'Home/index.html')

def login(request):

    return render(request, "Home/login.html")