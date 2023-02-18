from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context=context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)


def products_add_view(request):
    if request.method == 'GET':
        context = {'categories': Category.objects.all()}
        return render(request, 'product_add.html', context=context)
    product_data = {
        'name': request.POST.get('name'),
        'category': get_object_or_404(Category, category=request.POST.get('category')),
        'description': request.POST.get('description', None),
        'coast': request.POST.get('coast'),
        'image': request.POST.get('image')
    }
    product = Product.objects.create(**product_data)
    return redirect('product_detail', pk=product.pk)