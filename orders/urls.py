from django.urls import path
from . import views

urlpatterns = [

    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart_view, name='cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),

    path('increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),

    path('checkout/', views.checkout_view, name='checkout'),
    path('success/', views.success_view, name='success'),
]