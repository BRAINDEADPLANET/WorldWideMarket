from django.shortcuts import render
from .models import Product


# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    template = 'Products/index.html'
    return render(request, template, context)


def prod_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    template = 'Products/product_view.html'
    return render(request, template, context)
