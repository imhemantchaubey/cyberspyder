from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('result', views.result, name='result'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]