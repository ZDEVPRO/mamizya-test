from django.shortcuts import render, redirect
from home.models import *


def index(request):
    return render(request, 'home.html')


def shop(request):
    products = Product.objects.all().order_by('-id')
    count = products.count()
    context = {
        'products': products,
        'count': count
    }
    return render(request, 'shop.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def shop_detail(request, id):
    product = Product.objects.get(id=id)
    images = ImageItem.objects.filter(product__id=id)
    context = {
        'product': product,
        'images': images
    }

    return render(request, 'shop_detail.html', context)


def buy_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')

        print(product_title)
        print(fullname)
        print(phone)

    context = {
        'product': product
    }
    return render(request, 'buy_product.html', context)
