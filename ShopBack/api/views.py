from itertools import product

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category
from django.shortcuts import get_object_or_404


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description,
             'count': product.count, 'is_active': product.is_active,} for product in products]
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    categories = Category.objects.all()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    data = [{'id': category.id, 'name': category.name}]
    return JsonResponse(data, safe=False)

def category_products(request, id):
    category = get_object_or_404(Category, id = id)
    products = category.products_set.all()
    data = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description,
             'count': product.count, 'is_active': product.is_active} for product in products]
    return JsonResponse(data, safe=True)

def category_list(request):
    categories = Category.objects.all()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(data, safe=False)



