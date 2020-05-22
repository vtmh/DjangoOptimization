from django.urls import path

from . import views

urlpatterns = [
    # /login/
    path('', views.middleware, name="middleware"),
    path('add_session/', views.add_session, name="add_session"),
    path('remove_session/', views.remove_session, name="remove_session"),

]
