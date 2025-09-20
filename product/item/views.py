from django.shortcuts import render
from .models import Product

def landingPage(request):
    products = Product.objects.all()
    return render(request, 'landing/landing.html', {'products': products})

def menuPage(request):
    products = Product.objects.all()
    return render(request, 'navbar/menu.html', {'products': products})

def aboutPage(request):
    return render(request, 'navbar/about.html')