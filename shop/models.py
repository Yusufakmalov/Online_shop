from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

class DeletedProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted_name = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(auto_now_add=True)


class ProductDiscount(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2) 
    start_time = models.DateTimeField()  
    end_time = models.DateTimeField()  

    def __str__(self):
        return f"{self.discount}% discount on {self.product.name} from {self.start_time} to {self.end_time}"