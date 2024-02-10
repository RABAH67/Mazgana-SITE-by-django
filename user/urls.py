from django.urls import path 
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('registere/', views.CustemRegistrationView.as_view(),name="register"),
    path('login/',auth_view.LoginView.as_view(template_name='register.html',authentication_form=LoginForm),name="login"),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('profile/', views.profile,name="profile"),





]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
