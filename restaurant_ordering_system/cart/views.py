from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from restaurant_website.models import Menu


@require_POST
def cart_add(request, product_id):
    """Добавление товаров в корзину"""
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
        return redirect('restaurant_website:home_restaurant')  # Перенаправление на страницу корзины
    else:
        print("Form errors:", form.errors)  # Вывод ошибок формы для отладки
        return redirect('restaurant_website:product_detail', product_slug=product.slug)


@require_POST
def cart_remove(request, product_id):
    """Изменение количества товаров в корзине"""
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    cart.remove(product)
    return redirect('restaurant_website:home_restaurant')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    return cart


def product_detail(request, id, slug):
    product = get_object_or_404(Menu, id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'restaurant_website/product.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
