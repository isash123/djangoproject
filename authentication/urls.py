# -*- encoding: utf-8 -*-

from django.urls import path
from authentication import views 
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
]
