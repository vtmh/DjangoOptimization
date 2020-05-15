from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from Pizza.models import Pizza, Toppings, Type, Cheese
from Pizza.forms import ToppingsForm


def homepage(request):

    pizza = Pizza.objects.all()
    toppings = Toppings.objects.all()
    cheeses = Cheese.objects.all()

    toppings_form = ToppingsForm

    print(toppings_form)

    data = {
        'pizza': pizza,
        'toppings': toppings,
        'cheeses': cheeses,
        'toppings_form': toppings_form
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
        name="Sausage",
        type=Type.objects.get(name="Meat"),
        price="1.50",
    )

    Toppings.objects.get_or_create(
        name="Banana Peppers",
        type=Type.objects.get(name="Vegetable"),
        price="0.25",
    )

    Toppings.objects.get_or_create(
        name="Mushrooms",
        type=Type.objects.get(name="Vegetable"),
        price="0.15",
    )

    Cheese.objects.get_or_create(
        name="Cheddar",
        is_healthy=False,
        price=0.75,
    )

    #I don't think Gouda is actually healthy but let's pretend it is...
    Cheese.objects.get_or_create(
        name="Gouda",
        is_healthy=True,
        price=3.75,
    )

    print('Show toppings')
    all_toppings = Toppings.objects.all()

    print(all_toppings)

    return HttpResponseRedirect(reverse('homepage'))

