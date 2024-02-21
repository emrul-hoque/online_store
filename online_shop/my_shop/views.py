from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    #return render(request, 'store/product_list.html', {'products': products})
    return render(request, 'product_list.html', {'products': products})


def index(request):
    return HttpResponse("Hello, World!")
