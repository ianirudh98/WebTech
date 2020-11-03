from django.db import models
from carts.models import Cart
from .utils import unique_order_generator
import math
from django.db.models.signals import pre_save, post_save

ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
)


class Order(models.Model):
    order_id = models.CharField(max_length=50,blank=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status = models.CharField(max_length=120,default='created',choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(max_digits=100,decimal_places=2,default=50.00)
    order_total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)

    class Meta:
        verbose_name_plural = 'Order'
    
    def __str__(self):
        return self.order_id

    def update_total(self):
        shipping_total = self.shipping_total
        cart_total = self.cart.total
        total = math.fsum([cart_total, shipping_total])
        total = format(total, '.2f')
        self.order_total = total
        self.save()
        return total

def pre_save_create_order_id(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_generator(instance)

pre_save.connect(pre_save_create_order_id,sender=Order)

def post_save_cart_total(sender,instance,created,*args,**kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart_id = cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total,sender=Cart)

def post_save_order(sender,instance,created,*args,**kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order,sender=Order)