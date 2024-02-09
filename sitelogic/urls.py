from django.urls import path 
from . import views




urlpatterns = [
    
    path('', views.home,name="home"),
    path('etude-service/', views.etude,name="Studyservice"),
    path('tourist-service/', views.tourism,name="tourist"),
    path('bisnase-service/', views.bisnase,name="bisnes"),


]
