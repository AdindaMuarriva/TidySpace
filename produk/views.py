from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

def home(request):
    featured = Product.objects.all()[:4]

    return render(request, 'produk/home.html', {
        'featured': featured
    })


def daftar_produk(request):
    query = request.GET.get('q')

    produk_list = Product.objects.all()

    if query:
        produk_list = produk_list.filter(name__icontains=query)

    paginator = Paginator(produk_list, 4)

    page_number = request.GET.get('page')

    produk = paginator.get_page(page_number)

    return render(request, 'produk/daftar_produk.html', {
        'produk': produk,
        'query': query
    })


def detail_produk(request, id):
    produk = get_object_or_404(Product, id=id)

    related = Product.objects.exclude(id=id)[:4]

    return render(request, 'produk/detail_produk.html', {
        'produk': produk,
        'related': related
    })


def kontak(request):
    return render(request, 'produk/kontak.html')