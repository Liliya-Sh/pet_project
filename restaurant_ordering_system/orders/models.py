from django.db import models
from decimal import Decimal


class Menu(models.Model):
    """Блюда ресторана"""
    name_dish = models.CharField(max_length=50, verbose_name='Наименование блюда')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to="photo_dish", blank=True, default='Добавить изображение')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name_dish - self.price - self.image

class Order(models.Model):
    """Заказ, который сделал клиент"""
    STATUS_COOK = 'Приготовлен'
    STATUS_NOT_COOK = 'Готовится'
    STATUS_CHOIСES = [
        (STATUS_NOT_COOK, 'Готовится'),
        (STATUS_COOK, 'Приготовлен'),
    ]

    STATUS_DELIVERED = 'Доставлено'
    STATUS_NOT_DELIVERED = 'Доставляется'
    STATUS_CHOIСES_2 = [
        (STATUS_NOT_DELIVERED, 'Доставляется'),
        (STATUS_DELIVERED, 'Доставлено'),
    ]

    CHOICES_PAY = (
        ('card', 'Карта'),
        ('cash', 'Наличные')
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Код клиента')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Сумма заказа')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')
    payment_method = models.CharField(max_length=50, choices=CHOICES_PAY, verbose_name='Способ оплаты')
    status_cook = models.CharField(
        max_length=32,
        choices=STATUS_CHOIСES,
        default=STATUS_NOT_COOK,
        verbose_name='Статус готовности заказа')
    status_delivery = models.CharField(
        max_length=32,
        choices=STATUS_CHOIСES_2,
        default=STATUS_NOT_DELIVERED,
        verbose_name='Статус доставки блюда')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.creation_time - self.amount - self.comment - self.order_readiness - self.order_delivery

    def get_amount(self):
        amount = Decimal(0)
        for item in self.orderitem_set.all():
            amount += item.amount
        return amount


class OrderItem(models.Model):
    """Составляющие заказа"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    dish = models.ForeignKey(Menu, on_delete=models.PROTECT, null=True, verbose_name='Код блюда')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Сумма')
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name='Скидка')
    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.order - self.dish - self.quantity - self.price - self.discount

    @property
    def amount(self):
        return self.quantity * (self.price - self.discount)