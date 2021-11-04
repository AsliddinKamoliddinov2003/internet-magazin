from store.models import Category, SubCategory, Product
from shopping.utils import get_cart


def funk(request):
    products = Product.objects.filter().order_by("-price")[:8]
    categories = Category.objects.all()
    sub_cats = SubCategory.objects.all()
    biggest_price = Product.objects.filter().order_by("-price").first()
    small_price = Product.objects.filter().order_by("price").first()


    return {
        "products":products,
        "categories":categories,
        "sub_cats":sub_cats,
        "biggest_price":biggest_price,
        "small_price":small_price,
    }

