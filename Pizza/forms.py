from django.forms import ModelForm
from Pizza.models import Toppings, Type, Cheese
from django import forms


class ToppingsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ToppingsForm, self).__init__(*args, **kwargs)

        self.fields['name'].label_from_instance = self.label_from_instance
        self.fields['type'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        return obj.name

    #TODO Make these types generate from toppings model
    TYPES = [
        ("1", "Meat"),
        ("2", "Vegetable"),

    ]

    name = forms.ModelChoiceField(queryset=Toppings.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    price = forms.DecimalField(decimal_places=2, max_digits=300)


    class Meta:
        model = Toppings
        fields = ['name', 'price', 'type']


class CheesesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CheesesForm, self).__init__(*args, **kwargs)

        self.fields['name'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        return obj.name

    name = forms.ModelChoiceField(queryset=Cheese.objects.all())
    is_healthy = forms.BooleanField
    price = forms.DecimalField(decimal_places=2, max_digits=300)

    class Meta:
        model = Cheese
        fields = ['name', 'is_healthy', 'price']