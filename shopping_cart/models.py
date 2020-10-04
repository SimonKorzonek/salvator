from django.db import models
from products.models import Product
from users.models import Account
from phone_field import PhoneField


# update_cart view function - updating OrderItem instance
# owner of cart optional
# if owner exists populate delivery form with his account information
# registration form asking about first and last name and address
# "join us" instead of profile section
# no @login_required decorator in view finctions dealing with order



class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    delivery_option = models.CharField(max_length=30)
    option_price = models.IntegerField()
    pre_paid = models.BooleanField()

    def __str__(self):
        representation = f"{self.delivery_option} (+{self.option_price}zł)"
        return representation

    class Meta:
        verbose_name_plural = "deliveries"



class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    # DELIVERY
    delivery_option = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)

    # ADDRESS
    address = models.CharField(max_length=120, default=None, null=True)
    postcode = models.CharField(max_length=6, default=None, null=True)
    city = models.CharField(max_length=30, default=None, null=True)
    phone_number = PhoneField(blank=True, null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_items_number(self):
        return self.items.all().count()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def get_cart_plus_delivery(self):
        return sum([item.product.price for item in self.items.all()], self.delivery_option.option_price)

    def __str__(self):
        return str(self.date_ordered)




class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    token = models.CharField(max_length=120)
    order_id = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']