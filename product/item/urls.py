from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='home'),
    path('menu/', views.menuPage, name='menu'),
    path('about/', views.aboutPage, name='about'),
]
