# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, logout, profile
from django.contrib.auth.views import LogoutView
from  . import  views
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/', profile, name="profile"),
    path('logout/', logout, name="logout")
]
