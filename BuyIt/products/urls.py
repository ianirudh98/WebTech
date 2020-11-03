from django.urls import path,re_path
from products.views import (
    Shop_List,
    slug
    )

urlpatterns = [
    path('',Shop_List,name="shop"),
    path('<slug>',slug),
]