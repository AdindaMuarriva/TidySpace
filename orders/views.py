from django.shortcuts import render, redirect, get_object_or_404
from produk.models import Product
from .models import Order, OrderItem
from django.contrib import messages
from urllib.parse import quote

def add_to_cart(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session['cart'] = cart

    messages.success(request, 'Product added to cart')

    return redirect('cart')


def cart_view(request):

    cart = request.session.get('cart', {})

    items = []
    total = 0

    for id, qty in cart.items():

        product = Product.objects.get(id=id)

        subtotal = product.price * qty

        total += subtotal

        items.append({
            'product': product,
            'qty': qty,
            'subtotal': subtotal,
        })

    formatted_total = "{:,.0f}".format(total)

    return render(request, 'orders/cart.html', {
        'items': items,
        'total': formatted_total,
    })

def checkout(request):

    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    cart_items = []
    total = 0

    for id, qty in cart.items():

        product = Product.objects.get(id=id)

        subtotal = product.price * qty
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': qty,
            'subtotal': "{:,.0f}".format(subtotal)
        })

    if request.method == 'POST':

        order = Order.objects.create(
            customer_name=request.POST['name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
        )

        message = f"""Halo TidySpace,

Saya ingin melakukan pemesanan produk berikut:

"""

        for id, qty in cart.items():

            product = Product.objects.get(id=id)

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty
            )

            subtotal = product.price * qty

            message += (
                f"• {product.name}\n"
                f"  Qty      : {qty}\n"
                f"  Subtotal : Rp {subtotal:,.0f}\n\n"
            )

        message += (
            f"Total Pembayaran : Rp {total:,.0f}\n\n"
            f"Nama             : {request.POST['name']}\n"
            f"No HP            : {request.POST['phone']}\n"
            f"Alamat           : {request.POST['address']}\n\n"
            f"Terima kasih."
        )

        request.session['cart'] = {}

        return redirect(
            f"https://wa.me/6285296932721?text={quote(message)}"
        )

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total': "{:,.0f}".format(total)
    })

def remove_from_cart(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        del cart[id]

    request.session['cart'] = cart

    return redirect('cart')

def increase_quantity(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        cart[id] += 1

    request.session['cart'] = cart

    return redirect('cart')

def decrease_quantity(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:

        cart[id] -= 1

        if cart[id] <= 0:
            del cart[id]

    request.session['cart'] = cart

    return redirect('cart')

def checkout_view(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():

        product = Product.objects.get(id=product_id)

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    if request.method == 'POST':

        request.session['cart'] = {}

        return redirect('/orders/success/')

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })


def success_view(request):
    return render(request, 'orders/success.html')