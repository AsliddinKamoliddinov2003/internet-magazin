from django.db import models
from datetime import datetime, timezone


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="images/", null=True)
    slug  = models.CharField(max_length=255, null=True)
    
    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True, null=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    name = models.CharField(max_length=255)
    body = models.TextField()
    price = models.FloatField(default=5000)
    CONDITION = {
        ("1", "yangi"),
        ("2", "ishlatilgan"),
        ("3", "bepul")
    }
    condition = models.CharField(choices=CONDITION, max_length=10, default="1")
    image = models.ImageField(upload_to="images/", null=True)
    slug = models.CharField(max_length=255, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    availabilty = models.BooleanField(default=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True, null=True)

    def __str__(self):
        return self.name

    
    def is_new_product(self):
        time_delta = datetime.now(timezone.utc) - self.created_at
        return time_delta.seconds < 86400


    
class Product_image(models.Model):
    image = models.ImageField(upload_to="images/", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images", null=True)


class Product_size(models.Model):
    name = models.CharField(max_length=255, null=True) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_size",null=True)
    

class  Product_color(models.Model):
    name = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_colors",null=True)


    
