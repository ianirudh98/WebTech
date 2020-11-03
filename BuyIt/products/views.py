from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse
from django.views.generic import ListView,DetailView
from .models import Product, Shop, Product_Category


def slug(request,slug):
    shops = [s.shop_slug for s in Shop.objects.all()]
    if slug in shops:
        category = Product_Category.objects.filter(category__shop_slug = slug) 
        shop = Shop.objects.filter(shop_slug = slug)
        queryset = category
        context = {
            'category_list': queryset,
            'shop_list': shop
        }
        return render(request,"products/category.html",context)

    products = [p.category_slug for p in Product_Category.objects.all()]
    if slug in products:
        items = Product.objects.filter(category__category_slug = slug)
        queryset = items
        context = {
            "product_list": queryset
        }
        return render(request,"products/product_list.html",context)


    product = [p.slug for p in Product.objects.all()]
    if slug in product:
        details = Product.objects.filter(slug = slug)
        queryset = details
        context = {
            "detail_list": queryset
        }
        return render(request,"products/product_detail.html",context)
    
    raise Http404("Product does not exist")

def Shop_List(request):
    queryset = Shop.objects.all()
    context = {
        'shop_list': queryset
    }
    return render(request,"home/index.html",context)