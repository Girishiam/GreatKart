from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.store_page, name='store'),
    path('<slug:slug>/', views.store_page, name='products_by_category'),
    path('<slug:slug>/<slug:product_slug>',
         views.product_details, name='productdetails'),
]
