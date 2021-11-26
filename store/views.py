from django.shortcuts import render
from django.urls  import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import *
from .utils import filter_min_max



def search(request, products):
    word = request.GET.get('q',None)
    if word:
        return products.filter(Q(name__contains=word) | Q(body__contains=word))
    return None



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



def store(request):
    holat = request.GET.get('holat',None)
    if holat:
        products = Product.objects.filter(condition=holat)
        products = filter_min_max(request, products)
    else:
        products = Product.objects.all()
        products = filter_min_max(request, products) 
    
    if search(request, products):
        products=search(request,products)

    context = {
        "products":products,
        "word":products
    }
    return render(request, "store/product-listing.html", context)



def category_productsView(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(sub_category__category=category)
    products = filter_min_max(request, products)

    if search(request, products):
        products=search(request,products)

    context = {
        "products":products,
        "word":products
    }
    return render(request, "store/product-listing.html", context)


def sub_categoryView(request, sub_cat_slug, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=sub_cat_slug, category=category)
    products = Product.objects.filter(sub_category=subcategory)
    product = products.first()
    products = filter_min_max(request, products)

    if search(request, products):
        products=search(request,products)

    context = {
        "products":products,
        "product":product,
        "word":products
    }
    return render(request, "store/product-listing.html", context)







 