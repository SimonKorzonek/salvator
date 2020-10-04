from django.db import models
from products.models import Product
from phone_field import PhoneField
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_products = models.ManyToManyField(Product)
    address = models.CharField(max_length=120, default='address')
    postcode = models.CharField(max_length=6)
    city = models.CharField(max_length=30)
    phone_number = PhoneField(blank=True, null=True)

    def __str__(self):
        return self.user.username

