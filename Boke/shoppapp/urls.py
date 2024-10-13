from django.urls import path
from . import views

from django.urls import path
from.views import product_list, add_product, edit_product, delete_product, add_to_cart, cart, create_order

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', product_list, name='product_list'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('create_order/', create_order, name='create_order'),
]