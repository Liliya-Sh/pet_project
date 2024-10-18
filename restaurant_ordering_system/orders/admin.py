from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email', 'phone_number', 'address',
                    'creation_time', 'comment', 'requires_delivery',
                    'payment_state']
    list_display_links = ['first_name']
    list_filter = ['creation_time', 'payment_state']
    inlines = [OrderItemInLine]

