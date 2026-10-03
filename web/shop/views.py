from django.shortcuts import render

from .products import PRODUCTS


def home(request):
    return render(request, "shop/home.html", {"products": PRODUCTS})


def product(request, product_id):
    item = next(
        (product for product in PRODUCTS if product["id"] == product_id),
        None,
    )

    if item is None:
        return render(request, "shop/product.html", {"product": None})

    return render(request, "shop/product.html", {"product": item})


def cart(request):
    return render(request, "shop/cart.html")
