from django.urls import path
from . import views
from .api import *

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/', views.daftar_produk, name='daftar_produk'),
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),
    path('kontak/', views.kontak, name='kontak'),

    path(
        'api/products/',
        get_products
    ),

    path(
        'api/products/<int:id>/',
        get_product
    ),

    path(
        'api/products/create/',
        create_product
    ),

    path(
        'api/products/update/<int:id>/',
        update_product
    ),

    path(
        'api/products/delete/<int:id>/',
        delete_product
    ),
]
