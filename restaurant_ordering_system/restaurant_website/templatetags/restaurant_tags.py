from django import template

from restaurant_website.utils import menu

register = template.Library()


@register.simple_tag
def get_menu():
    return menu
