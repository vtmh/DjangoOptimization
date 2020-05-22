from django.urls import path

from . import views

urlpatterns = [
    # /login/
    path('', views.middleware, name="middleware"),



]