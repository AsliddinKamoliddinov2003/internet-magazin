from django.db import models
from django.contrib.auth import get_user_model

from  store.models import Product

User = get_user_model()



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True)
