from django.shortcuts import render, redirect, reverse
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    queryset = Product.objects.all()
    context = {
        'products':queryset,
        "app_name": 'Aviato | Home',
    }
    return render(request, 'index.html', context)


@login_required
def product_shop(request):
    queryset = Product.objects.all()
    context = {
        "products": queryset,
        "app_name": "Aviato | Shop"
    }
    return render(request, 'shop.html', context)
