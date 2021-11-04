from django.urls import path

from .views import add_cart_item, cart, minus_cart_item, remove_cart_item, standalone

urlpatterns = [
    path("add-cart-item/<int:product_id>/", add_cart_item, name="add-cart-item"),
    path("minus-cart-item/<int:product_id>/", minus_cart_item, name="minus-cart-item"),
    path("remove-cart-item/<int:product_id>/", remove_cart_item, name="remove-cart-item"),
    path("cart/", cart, name="cart"),
    path("standalone/", standalone, name="standalone"),
]