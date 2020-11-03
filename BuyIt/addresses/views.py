from django.shortcuts import render, redirect
from .forms import AddressForm
from django.conf import settings

User = settings.AUTH_USER_MODEL

def address(request):
    form = AddressForm(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        form.save()
        context['form'] = AddressForm()
        return redirect("cart")

    return render(request,"carts/address.html",context) 