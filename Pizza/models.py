from django.db import models

# Create your models here.

class Toppings(models.Model):
    name = models.CharField(max_length=100)
    type = None
    price = models.DecimalField

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Toppings)
    cheese = None
    price = models.DecimalField
    total_price = models.DecimalField(null=True)


class Cheese(models.Model):
    name = models.CharField(max_length=100)
    is_healthy = models.BooleanField
    price = models.DecimalField


class type(models.Model):
    name = models.CharField(max_length=20)