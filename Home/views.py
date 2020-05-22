from django.shortcuts import render, redirect
from .forms import LoginForm
from django.db import connection
from .models import LoginEntry
from django.utils import timezone

# Create your views here.

def homepage(request):

    logins = LoginEntry.objects.all()

    return render(request, 'Home/index.html', {
        'logins': logins,
    })

def login(request):

    form = LoginForm
    cursor = connection.cursor()

    if request.method == 'POST':
        print('form submitted')
        clean_form = LoginForm(request.POST)

        if clean_form.is_valid():
            print('form valid')
            request.session['name'] = clean_form.cleaned_data['user_name']
            ##create new login entry

            LoginEntry.objects.create()



            return redirect('homepage')


    return render(request, "Home/login.html", {
        'form': form,
    })