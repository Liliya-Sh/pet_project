from django.contrib import admin
from .models import Menu, Category, Messages


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'slug', 'description', 'price', 'created', 'is_available']
    list_display_links = ['name_product']
    list_filter = ['is_available', 'created']
    list_editable = ['price', 'is_available']
    prepopulated_fields = {'slug': ('name_product',)}
    list_per_page = 10


admin.site.register(Menu, MenuAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'phone', 'email', 'message', 'created']
    list_display_links = ['email']
    list_filter = ['email', 'created']


admin.site.register(Messages, MessagesAdmin)
