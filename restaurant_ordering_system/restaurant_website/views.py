from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView

from cart.cart import Cart
from cart.forms import CartAddProductForm
from cart.views import cart_detail
from .forms import MessagesForm

from .models import *
from .utils import menu


def home_restaurant(request):
    """Главная страница пиццерии с Меню и корзиной"""
    product = Menu.available.all()
    category = Category.objects.all()
    cart_product_form = CartAddProductForm
    cart = Cart(request)
    cart = cart_detail(cart)

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'product': product,
        'category': category,
        'cart_product_form': cart_product_form,
        'cart': cart,
    }
    return render(request, 'restaurant_website/home_restaurant.html', context=data)


def product_detail(request, product_slug):
    """Просмотреть отдельный товар"""
    product = get_object_or_404(Menu, slug=product_slug)
    cart_product_form = CartAddProductForm()
    data = {
        'menu': menu,
        'product': product,
        'cart_product_form': cart_product_form,
     }
    return render(request, 'restaurant_website/product.html', context=data)


class HomePageView(ListView):
    model = Menu
    template_name = 'product.html'
    template_name1 = 'home_restaurant.html'


def about(request):
    """Отправить сообщение пиццерии"""
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение отправлено')
            return redirect('restaurant_website:about',)
    else:
        form = MessagesForm

    return render(request,'restaurant_website/about.html',
                  {'form': form})


def stocks(request):
    """Страница с акциями"""
    return render(request, 'restaurant_website/stocks.html', {'menu': menu})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
