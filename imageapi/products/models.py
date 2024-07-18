from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=200)


    def __str__(self):
        return self.title

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name="image")
    image=models.ImageField(upload_to='img', blank=True, null=True)