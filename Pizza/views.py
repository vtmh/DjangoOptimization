from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from Pizza.models import Pizza, Toppings, Type, Cheese
from Pizza.forms import ToppingsForm, CheesesForm, RegularForm


def homepage(request):
    pizza = Pizza.objects.all()
    toppings = Toppings.objects.all()
    cheeses = Cheese.objects.all()

    toppings_form = ToppingsForm
    cheeses_form = CheesesForm
    regular_form = RegularForm

    data = {
        'pizza': pizza,
        'toppings': toppings,
        'cheeses': cheeses,
        'toppings_form': toppings_form,
        'cheeses_form': cheeses_form,
        'regular_form': regular_form,
    }

    if request.method == "POST":
        form_toppings = ToppingsForm(request.POST)
        form_cheeses = CheesesForm(request.POST)
        regular_form = RegularForm(request.POST)

        if form_toppings.is_valid() and form_cheeses.is_valid():
            print("Form submitted successfully")
            # Create the pizza here
            topping = form_toppings.cleaned_data['type'].name
            cheese = form_cheeses.cleaned_data['name'].name

            pizza_name = form_cheeses.cleaned_data['name'].name + " pizza"
            #TODO Make this value not hardcoded
            size = "large"
            new_pizza = Pizza.objects.create(
                name=pizza_name,
                size=size,
                # toppings=form_toppings, You can't assign a many to many field during instance creation. You must first create the object.
                cheese=Cheese.objects.get(name=cheese),
                price=0,
                total_price=0,
            )

            new_pizza.toppings.add(Toppings.objects.get(name=topping))
            print("Pizza has been created! Yum!")

        if regular_form.is_valid():
            print("Regular form submitted")

            pizza_name = regular_form.cleaned_data['cheese_choice'].name + " pizza"
            size = regular_form.cleaned_data['size']
            topping = regular_form.cleaned_data['topping_type'].name
            cheese = regular_form.cleaned_data['cheese_choice'].name

            new_pizza = Pizza.objects.create(
                name=pizza_name,
                size=size,
                cheese=Cheese.objects.get(name=cheese),
                price=0,
                total_price=0,
            )
            new_pizza.toppings.add(Toppings.objects.get(name=topping))
            print("Regular form pizza created")

    return render(request, 'Pizza/index.html', data)


def seed_toppings(request):
    # Create a pizza

    # Init Types for toppings

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

    # I don't think Gouda is actually healthy but let's pretend it is...
    Cheese.objects.get_or_create(
        name="Gouda",
        is_healthy=True,
        price=3.75,
    )

    print('Show toppings')
    all_toppings = Toppings.objects.all()

    print(all_toppings)

    return HttpResponseRedirect(reverse('homepage'))

def query_testing(request):
    pizzas = Pizza.objects.prefetch_related('toppings')


    #This makes 28 queries! holy cow (with no optimizations)

    # This makes 15 queries with prefetch_related...
    # Toppings is a Many to Many field on Pizza, which is why I used prefetch_related and not select_related.
    # pre_fetch related works by having the SQL JOIN be made using Python rather than the database.
    # The database is no longer pinged for each call, just the inital Pizza call

    for pizza in pizzas:  # 1 query is here
        print(pizza.toppings.all)
        for topping in pizza.toppings.all():  # 1 query is here
            print(topping.name, topping.price)  # 2 queries are here for each topping, this adds up very quickly
            print(topping.type.name)  # more queries here for each topping….
        print(pizza.cheese.name)  # and without optimization another one here...





    return render(request, 'Pizza/query.html')