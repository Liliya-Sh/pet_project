from django.urls import path, register_converter, converters
from . import views
from .views import HomePageView

app_name = 'restaurant_website'
# register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.home_restaurant, name='home_restaurant'),
    path('about/', views.about, name='about'),
    path('product/<slug:product_slug>', views.product_detail, name='product_detail'),
    path('stocks/', views.stocks, name='stocks'),
    path('product/', HomePageView.as_view, name='product'),
    path('', HomePageView.as_view, name='home_restaurant'),
]
