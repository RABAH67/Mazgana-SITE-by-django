from django.urls import path 
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm



urlpatterns = [
    
    path('registere/', views.CustemRegistrationView.as_view(),name="register"),
    path('login/',auth_view.LoginView.as_view(template_name='register.html',authentication_form=LoginForm),name="login"),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),





]
