from django.shortcuts import render
from products.models import Product


def home(request):
    context = {
        'products': Product.objects.all()}
    return render(request, 'shop/home.html', context)


def about(request):
    return render(request, 'shop/about.html')
