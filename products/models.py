from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    short_description = models.TextField(default='product list description')
    long_description = models.TextField(default='product detail description')
    availability = models.BooleanField()
    discount = models.FloatField(default='0')
    quantity_available = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')

    def __str__(self):
        return f'{self.name}'
