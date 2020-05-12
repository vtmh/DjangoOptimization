# DjangoOptimization
Idea: This mini-project will be used to teach you the optimization issues apparent in Django. You will explore all of the various relationships provided between models and figure out how to optimize the queries to not destroy performance of the app.

1) Create a base Django project using SQLite, this will be a “pizza” application

2) Install Django Debug Toolbar (allows you to see queries)

3) Models

Pizza
Name
Size
Toppings (Many 2 Many with Topping Model)
Cheese (Foreign Key)
Price (Decimal)
Total Price (Nullable Decimal, will be updated in a signal in step 11)

Topping
Name
Type (Foreign Key to Type)
Price

Cheese
Name
is_healthy (boolean)
Price (normally this wouldn’t cost extra but it is easier for this exercise)

Type
Name (Vegetable or Meat, or whatever...)

4) Create a seed method that adds items to Topping and Cheese, and then also have a seed method that seeds built pizzas (this will make testing this much easier for you)

5) Seed a bit of data

6) Create a ModelForm that allows you to select from the available Toppings and cheeses in order to build a pizza and store it into the system

7)  Create a regular Form that allows you to select from the available Toppings and cheeses in order to build a pizza and store it into the system

Now let’s mess around with optimization…
8) Loop over entered pizzas inside a template and follow this pseudocode





for pizza in pizzas:  # 1 query is here
    for topping in pizza.toppings.all: # 1 query is here
        print(topping.name, topping.price) # 2 queries are here for each topping, this adds up very quickly
        print(topping.type.name) # more queries here for each topping….
     print(pizza.cheese.name) # and without optimization another one here...

- notice the comments above and look at Django Debug Toolbar to see the issues

9) Learn how select_related() and prefetch_related() can be used to reduce queries.

10) After you get prefetch to work, re-filter the queryset, you will see that the prefetching is broken and new queries are made...for example:

for pizza in pizzas:  
    # if you are prefetched this will not hit the DB anymore
    for topping in pizza.toppings.all:
         print(topping.name)

    # now watch it break due to new filter, learn why this happens...
    toppings =  pizza.toppings.filter(price > 5.00)
    for topping in toppings:
         print(topping.name)
   

10) Create Model Methods for Pizza that gather the total price of the pizza based on all elements in it.

11) Create a presave signal for the pizza model, when the model is saved update the Total Price to hold the value of the price of the pizza + all toppings and cheese

12) Create a postsave signal for the pizza model, after the model is saved update the Total Price to hold the value of the price of the pizza + all toppings and cheese and then pizza.save() again…notice the strange error you will get with infinite looping. Now you know why our postsave signals only alter alternative models.
