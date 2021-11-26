from django.contrib import admin

from .models import *


class ProductImageAdmin(admin.StackedInline):
    model = Product_image
    fields = ["image"]
    extra = 1


class ProductColorStackedAdmin(admin.StackedInline):
    model = Product_color
    fields = ["name"]
    extra = 1



class ProductSizeStackedAdmin(admin.StackedInline):
    model = Product_size
    fields = ["name"]
    extra = 1



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display=["name", "price", "sub_category", "is_active"]
    list_display_links=["name"]
    search_fields=["name","description"]
    prepopulated_fields={"slug":("name",)}
    
    inlines = [ProductImageAdmin, ProductColorStackedAdmin, ProductSizeStackedAdmin]



admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)



