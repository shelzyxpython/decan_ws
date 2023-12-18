from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import AddProduct


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('test')


def end(request):
    return HttpResponse('Спасибо за покупку!')


def cart(request):
    products = Product.objects.all()
    return render(request, 'cart.html', {'products': products})


def create_view(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            create = Product.objects.create(name=name, description=description, price=price)
            create.save()
            return redirect('items')
    form = AddProduct()
    return render(request, 'create_product.html', context={'form': form})