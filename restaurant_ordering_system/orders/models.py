from django.contrib.auth import get_user_model
from django.db import models

from restaurant_website.models import Menu


class Order(models.Model):
    """Заказ, который сделал клиент"""
    objects = None

    PAYMENT_ON_GET = 'Оплата при получении'
    PAYMENT_BY_CARD = 'Оплата картой'
    PAYMENT_STATE = [
        (PAYMENT_ON_GET, 'Оплата при получении'),
        (PAYMENT_BY_CARD, 'Оплата картой'),
    ]

    user = models.ForeignKey(get_user_model(),
                             on_delete=models.SET_NULL,
                             related_name='orders',
                             null=True,
                             blank=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=35, verbose_name="Номер телефона")
    address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')
    payment_state = models.CharField(
        max_length=32,
        choices=PAYMENT_STATE,
        default=PAYMENT_BY_CARD,
        verbose_name='Способ оплаты')

    class Meta:
        ordering = ['pk']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Составляющие заказа"""
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Menu,
                                related_name='order_items',
                                on_delete=models.CASCADE,
                                verbose_name='Код блюда')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Сумма')
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name='Скидка в %')

    class Meta:
        ordering = ['pk']

    def get_cost(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return str(self.id)
