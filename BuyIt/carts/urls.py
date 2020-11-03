from django.urls import path,re_path
from .views import (
    cart_view,
    update_cart,
    )

urlpatterns = [
    path('',cart_view,name="cart"),
    path('<slug>',update_cart,name="update"),
]