from django.urls import path,re_path
from .views import (
    view_list,
    update_list
    )

urlpatterns = [
    path('',view_list,name="wishlist"),
    path('<slug>',update_list,name="list_update")
]