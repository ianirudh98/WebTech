from django.db import models
from products.models import Product


class Wishlist(models.Model):
    products = models.ManyToManyField(Product,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Wishlist"

    def __str__(self):
        return str(self.id)