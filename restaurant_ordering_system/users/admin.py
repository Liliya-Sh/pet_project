from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'password', 'email', 'phone', 'is_active']
    list_display_links = ['first_name']


admin.site.register(User, UserAdmin)
