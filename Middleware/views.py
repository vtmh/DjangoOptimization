from django.shortcuts import render

# Create your views here.

def middleware(request):


    return render(request, 'Middleware/index.html')