from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from restaurant_website.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('restaurant_website.urls', namespace='restaurant')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
