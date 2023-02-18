from django.urls import path

from webapp.views.categories import category_add
from webapp.views.products import products_view, product_view

urlpatterns = [
    path('', products_view, name='index'),
    path('products', products_view, name='products_view'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('categories/add', category_add, name='category_add')
]