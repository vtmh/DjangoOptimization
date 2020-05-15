from django.shortcuts import render

# Create your views here.
from Pizza.models import Pizza


def homepage(request):

    # pizza_count = Pizza.objects
    # print(pizza_count)

    return render(request, 'Pizza/index.html')

def seed_pizza(request):

    return None