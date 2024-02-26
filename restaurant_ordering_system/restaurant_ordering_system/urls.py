from django.contrib import admin
from django.urls import path, include
from orders import views
from orders.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include("django.contrib.auth.urls")),
]

handler404 = page_not_found
