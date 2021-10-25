from django.shortcuts import render
from django.urls  import reverse
from django.shortcuts import get_object_or_404

from .models import *



def homeView(request):
    
    return render(request, 'index/index-shop.html')



def detailView(request, slug):
    product = Product.objects.filter(slug=slug)

    if not product.exists():
        return render(reverse("home-view"))
    else:
        product = product.first()

    context = {
        "product":product,
    }

    return render(request, "index/product-detail.html", context)


def category_productsView(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(sub_category__category=category)

    context = {
        "products":products,
    }

    return render(request, "store/product-listing.html", context)


def sub_categoryView(request, sub_cat_slug, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=sub_cat_slug, category=category)
    products = Product.objects.filter(sub_category=subcategory)
    product = products.first()

    context = {
        "products":products,
        "product":product,
    }

    return render(request, "store/product-listing.html", context)







 