from django.urls import path
from .views import *



urlpatterns = [
    path('', homeView, name='home-view'),
    path('detail/<slug:slug>/', detailView, name='detail-view'),
    path('store/', store, name="store"),
    path('store/<slug:category_slug>/', category_productsView, name='category-products'),
    path('store/<slug:category_slug>/<slug:sub_cat_slug>/', sub_categoryView, name='subcategory-products'),
]