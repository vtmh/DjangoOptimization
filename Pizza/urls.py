from django.urls import path

from . import views

urlpatterns = [
    # /login/
    path('', views.homepage, name="homepage"),
    path('seed_toppings/', views.seed_toppings, name="seed_toppings")


]