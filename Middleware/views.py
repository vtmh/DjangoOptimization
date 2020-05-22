from django.shortcuts import render, redirect

# Create your views here.

def middleware(request):



    return render(request, 'Middleware/index.html')

def add_session(request):

    request.session['name'] = "Marcus"

    return redirect('middleware')

def remove_session(request):



    if 'name' in request.session:
        del request.session['name']

    return redirect('middleware')

