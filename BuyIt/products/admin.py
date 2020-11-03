from django.contrib import admin
from .models import Product, Shop, Product_Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Product


class ShopAdmin(admin.ModelAdmin):
    list_display = ['__str__','shop_slug']
    class Meta:
        model = Shop

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__','category']
    class Meta:
        model = Product_Category

admin.site.register(Product,ProductAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(Product_Category,CategoryAdmin)