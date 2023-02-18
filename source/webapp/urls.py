from django.urls import path

from webapp.views.products import products_view

urlpatterns = [
    path('', products_view)
]