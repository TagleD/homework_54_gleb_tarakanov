from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.models import Category


def category_add(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'category_add.html')
    category_data = {
        'category': request.POST.get('category'),
        'description': request.POST.get('description', None)
    }
    Category.objects.create(**category_data)
    return redirect('products_view')