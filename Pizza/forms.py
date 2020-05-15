from django.forms import ModelForm
from Pizza.models import Toppings, Type, Cheese
from django import forms


class ToppingsForm(ModelForm):
    ##Pulled  this from stackoverflow - Allows me to add labels onto select values so it doesn't just say object.
    def __init__(self, *args, **kwargs):
        super(ToppingsForm, self).__init__(*args, **kwargs)

        self.fields['name'].label_from_instance = self.label_from_instance
        self.fields['type'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        return obj.name



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


class RegularForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegularForm, self).__init__(*args, **kwargs)

        self.fields['topping_type'].label_from_instance = self.label_from_instance
        self.fields['topping_type2'].label_from_instance = self.label_from_instance
        self.fields['topping_type3'].label_from_instance = self.label_from_instance
        self.fields['cheese_choice'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        return obj.name

    size_choices = [
        ('large', 'large'),
        ('medium', 'medium'),
        ('small', 'small'),
    ]

    topping_type = forms.ModelChoiceField(queryset=Toppings.objects.all())
    topping_type2 = forms.ModelChoiceField(queryset=Toppings.objects.all())
    topping_type3 = forms.ModelChoiceField(queryset=Toppings.objects.all())
    cheese_choice = forms.ModelChoiceField(queryset=Cheese.objects.all())
    size = forms.ChoiceField(choices=size_choices)