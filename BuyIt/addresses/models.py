from django.db import models
from billings.models import BillingProfile
from django.conf import settings
from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=200)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120,default="India")
    postal_code = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return str(self.billing_profile)

#     def create_billing_user(sender,instance,created,*args,**kwargs):
#         if not created:


# pre_save.connect(create_billing_user,sender=User)