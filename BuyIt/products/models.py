import random
import os
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,1000)
    name,ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/product_images/{final_filename}".format(final_filename=final_filename)

def upload_shop_image_path(instance,filename):
    new_filename = random.randint(1,1000)
    name,ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "shop/shop_images/{final_filename}".format(final_filename=final_filename)


class Product(models.Model):
    title = models.CharField(max_length=50,null=True)
    slug = models.SlugField(blank=True,unique=True,primary_key=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=30)
    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    category = models.ForeignKey('Product_Category',on_delete=models.CASCADE,default='all')

    class Meta:
        verbose_name_plural = "Product"

    def get_absolute_url(self):
        return "{slug}".format(slug=self.slug)

    def __str__(self):
        return self.title

def pre_save_create_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_create_slug,sender=Product)


class Shop(models.Model):
    category = models.CharField(max_length=10,unique=True)
    shop_slug = models.SlugField(blank=True,unique=True)
    image = models.ImageField(upload_to=upload_shop_image_path,null=True,blank=True)
    display = models.ImageField(upload_to=upload_shop_image_path,null=True,blank=True)
    image1 = models.ImageField(upload_to=upload_shop_image_path,null=True,blank=True)
    image2 = models.ImageField(upload_to=upload_shop_image_path,null=True,blank=True)
    image3 = models.ImageField(upload_to=upload_shop_image_path,null=True,blank=True)
    image4 = models.ImageField(upload_to=upload_shop_image_path,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Shop"

    def __str__(self):
        return self.category


class Product_Category(models.Model):
    sub_category = models.CharField(max_length=20)
    category_slug = models.SlugField(primary_key=True,blank=True)
    category = models.ForeignKey(Shop,on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.sub_category