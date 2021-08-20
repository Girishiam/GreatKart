from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('place_order', views.palce_order, name='palce_order'),
    path('payments', views.payments, name='payments'),
    path('order_complete', views.order_complete, name='order_complete'),


]
