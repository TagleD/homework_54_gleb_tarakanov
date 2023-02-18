from django.urls import path

from webapp.views.categories import category_add_view
from webapp.views.products import products_view, product_view, products_add_view

urlpatterns = [
    path('', products_view, name='index'),
    path('products', products_view, name='products_view'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('categories/add', category_add_view, name='category_add'),
    path('products/add', products_add_view, name='products_add')
]