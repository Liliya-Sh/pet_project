from django.shortcuts import render

from cart.cart import Cart
from cart.views import cart_detail
from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    """Сосдание заказа"""
    cart = Cart(request)
    cart = cart_detail(cart)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистить корзину
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order}
                          )
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
