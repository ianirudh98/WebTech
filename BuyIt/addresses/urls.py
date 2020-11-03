from django.urls import path,re_path
from .views import (
    address
    )

urlpatterns = [
    path('address/',address,name="address"),
]