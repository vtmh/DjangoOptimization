from django.db import models

# Create your models here.

class Type (models.Model):
    name = models.CharField(max_length=20) #Meat, Cheese, Etc


class Toppings(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=300)


class Cheese(models.Model):
    name = models.CharField(max_length=100)
    is_healthy = models.BooleanField
    price = models.DecimalField(decimal_places=2, max_digits=300)


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Toppings)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=300)
    total_price = models.DecimalField(null=True, decimal_places=2, max_digits=300)
