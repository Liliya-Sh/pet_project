from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000/
    path('cook/', views.cook, name='cook'),    #http://127.0.0.1:8000/cook/
    path('delivery/', views.deliveryman, name='delivery'),   #http://127.0.0.1:8000/delivery/

]