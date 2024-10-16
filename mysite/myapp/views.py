from django.shortcuts import render

from .models import Product



def index(request):

    products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, "myapp/index.html", context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    print(product)
    context = {
        "product": product
    }
    return render(request, "myapp/detail.html", context)
