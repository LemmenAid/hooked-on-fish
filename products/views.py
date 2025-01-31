from django.shortcuts import render, get_object_or_404
from .models import Product


def global_context(request):
    """ Context processor to make products available in all templates """
    products = Product.objects.all()
    return {'nav_products': products}


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
