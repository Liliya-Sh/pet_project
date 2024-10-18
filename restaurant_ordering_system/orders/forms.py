from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Форма для создания заказа."""
    class Meta:
        model = Order
        fields = ['first_name', 'phone_number', 'email', 'address',
                  'comment', 'requires_delivery', 'payment_state']
