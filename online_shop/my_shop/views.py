from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def product_list(request):
    products = Product.objects.all()
    #return render(request, 'store/product_list.html', {'products': products})
    return render(request, 'product_list.html', {'products': products})


def index(request):
    store_name = "Welome to Kachchi Bhai! Your favourite biriyani place"  # Set your store name here
    return render(request, 'index.html', {'store_name': store_name})

