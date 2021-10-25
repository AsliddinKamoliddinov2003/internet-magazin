from store.models import Category, SubCategory, Product


def funk(request):
    products = Product.objects.filter().order_by("-price")[:8]
    categories = Category.objects.all()
    sub_cats = SubCategory.objects.all()

    return {
        "products":products,
        "categories":categories,
        "sub_cats":sub_cats
    }

