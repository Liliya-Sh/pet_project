from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс пользователя"""

    class Positions(models.TextChoices):
        DIRECTOR = 'Director'
        COOK = 'Cook'
        DELIVERER = 'Deliverer'
        CUSTOMER = 'Customer'
        ADMIN = 'Admin'

    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес доставки', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    position = models.CharField(max_length=30, verbose_name='Должность', null=True, blank=True,
                                choices=Positions.choices, default=Positions.CUSTOMER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('first_name',)
