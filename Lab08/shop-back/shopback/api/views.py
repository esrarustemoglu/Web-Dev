from django.shortcuts import render
from .models import Product, Category
from django.http import JsonResponse

def products (request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    return JsonResponse(data)
def products_by_id(request, id):
    try:
        product = Product.objects.get(id = id)
        return JsonResponse({
            "id" : product.id,
            "name" : product.name,
            "price" : product.price,
            "description" : product.description,
            "count": product.count,
            "is_active": product.is_active,
            "category_id": product.category_id
        })
    except Product.DoesNotExist:
        return JsonResponse({"Product not found!"}, status = 404)
def categories (request):
    categories = Category.objects.all()
    data = {"categories": list(categories.values())}
    return JsonResponse(data)
def category_by_id(request, id):
    try:
        category = Category.objects.get(id = id)
        return JsonResponse({
            "id" : category.id,
            "name" : category.name 
        })
    except Category.DoesNotExist:
        return JsonResponse({"Category not found!"}, status = 404)
def products_by_category(request, id):
    try:
        category = Category.objects.get(id = id)
        product = Product.objects.filter(category = category)
        return JsonResponse({
            "products" : list(product.values())
        })
    except Category.DoesNotExist:
        return JsonResponse({"Category does not exist"}, status = 404)


# Create your views here.
