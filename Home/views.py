from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.

def homepage(request):

    return render(request, 'Home/index.html')

def login(request):

    form = LoginForm

    if request.method == 'POST':
        print('form submitted')
        clean_form = LoginForm(request.POST)

        if clean_form.is_valid():
            print('form valid')
            request.session['name'] = clean_form.cleaned_data['user_name']
            return redirect('homepage')


    return render(request, "Home/login.html", {
        'form': form,
    })