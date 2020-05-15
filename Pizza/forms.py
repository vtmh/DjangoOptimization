from django.forms import ModelForm
from Pizza.models import Toppings, Type
from django import forms


class ToppingsForm(ModelForm):

    #TODO Make these types generate from toppings model
    TYPES = [
        ("1", "Meat"),
        ("2", "Vegetable"),

    ]

    name = forms.CharField(max_length=100)
    type = forms.ChoiceField(choices=TYPES)
    price = forms.DecimalField(decimal_places=2, max_digits=300)

    class Meta:
        model = Toppings
        fields = ['name', 'price', 'type']


