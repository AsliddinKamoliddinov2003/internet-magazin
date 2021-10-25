from django.db import models
from django.contrib.auth import get_user_model

from  store.models import Product



class Cart(models.Model):
    session_id = models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    color = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True)

    
    def total_price(self):
        return self.quantity * self.product.price
