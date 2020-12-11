from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', register, name='blog-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='blog-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='blog-logout'),
    path('profile/', profile, name='blog-profile'),

]