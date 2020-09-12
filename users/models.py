from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Account(models.Model):
    # declaring relationship with existing user model provided by django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_products = models.ManyToManyField(Product)
    address = models.CharField(max_length=120, default='address')
    postcode = models.CharField(max_length=6)
    city = models.CharField(max_length=30)
    phone_number = models.IntegerField(default=False, null=True)


    def __str__(self):
        return self.user.username

