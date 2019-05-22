from django.contrib import admin
from django.urls import path, include
from .views import reg,profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html') , name="users-logout"),
    path('register/', reg , name="users-register"),
    path('profile/', profile , name="users-profile"),
]