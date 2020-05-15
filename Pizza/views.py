from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from Pizza.models import Pizza, Toppings, Type


def homepage(request):

    pizza = Pizza.objects.all()
    toppings = Toppings.objects.all()

    data = {
        'pizza': pizza,
        'toppings': toppings,
    }

    return render(request, 'Pizza/index.html', data)

def seed_toppings(request):
    #Create a pizza

    #Init Types for toppings

    meat = Type.objects.get_or_create(
        name="Meat"
    )

    vegetable = Type.objects.get_or_create(
        name="Vegetable"
    )

    print(meat)
    print(vegetable)

    Toppings.objects.get_or_create(
        name="Pepporoni",
        type=Type.objects.get(name="Meat"),
        price="0.50",
    )

    Toppings.objects.get_or_create(
        name="Banana Peppers",
        type=Type.objects.get(name="Vegetable"),
        price="0.25",
    )

    print('Show toppings')
    all_toppings = Toppings.objects.all()

    print(all_toppings)

    return HttpResponseRedirect(reverse('homepage'))

