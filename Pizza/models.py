from django.db import models

# Create your models here.

# Notes...
# Use select_related when the object I want is a single object (AKA, ForeignKey, OneToOne).
# Use prefetch_related when you want to get a set of things (Many To many, probably other things)

class Type (models.Model):
    name = models.CharField(max_length=20) #Meat, Cheese, Etc


class Toppings(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=300)



class Cheese(models.Model):
    name = models.CharField(max_length=100)
    is_healthy = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=300)


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Toppings)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=300)
    total_price = models.DecimalField(null=True, decimal_places=2, max_digits=300)


    def total_pizza_price(self):
        print(self.total_price)
        pizza_toppings = self.toppings.all()
        calc_pric = 0
        for topping in pizza_toppings:
            print(topping.price)
            calc_pric += topping.price
        self.total_price = calc_pric
        print('total toppings cost')
        print(calc_pric)




