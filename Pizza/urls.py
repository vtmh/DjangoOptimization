from django.urls import path

from . import views

urlpatterns = [
    # /login/
    path('', views.homepage, name="homepage"),


]