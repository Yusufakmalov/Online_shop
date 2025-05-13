from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.filter(active=True)
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


