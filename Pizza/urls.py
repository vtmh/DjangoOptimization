from django.urls import path

from . import views

urlpatterns = [
    # /login/
    path('', views.homepage, name="homepage"),
    path('query/', views.query_testing, name="query"),
    path('seed_toppings/', views.seed_toppings, name="seed_toppings")


]