from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Billing Profile"
    
    def __str__(self):
        return str(self.user)
    
def user_created_reciever(sender,instance,created,*args,**kwargs):
    if created:
        BillingProfile.objects.get_or_create(user=instance,email=instance.email)

post_save.connect(user_created_reciever,sender=User)