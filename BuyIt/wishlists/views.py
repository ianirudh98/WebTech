from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Wishlist
from products.models import Product


def view_list(request):
    try:
        the_id = request.session['wishlist_id']
    except:
        the_id = None
    
    if the_id:
        item = Wishlist.objects.get(id = the_id)
        context = {
            "list":item
        }
    else:
        empty_message = "Wishlist is Empty!"
        context = {
            "empty": True,
            "empty_message": empty_message
        }

    return render(request,"wishlist/wishlist.html",context)


def update_list(request,slug):
    try:
        the_id = request.session['wishlist_id']
    except:
        new_list = Wishlist()
        new_list.save()
        request.session['wishlist_id'] = new_list.id
        the_id = new_list.id

    wishlist = Wishlist.objects.get(id = the_id)

    try:
        item = Product.objects.get(slug = slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    if not item in wishlist.products.all():
        wishlist.products.add(item)
    else:
        wishlist.products.remove(item)

    return redirect(reverse("wishlist"))