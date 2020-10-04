from django.db import models
from multiselectfield import MultiSelectField


categories = ((1, 'kawy'),
              (2, 'fartuchy'),
              (3, 'akcesoria'),
              (5, 'inne'))

class Product(models.Model):
    name = models.CharField(max_length=120)
    category = MultiSelectField(choices=categories, default=1, max_choices=1)
    short_description = models.TextField(default='product list description')
    long_description = models.TextField(default='product detail description')
    availability = models.BooleanField()
    discount = models.FloatField(default='0')
    quantity_available = models.IntegerField()
    price = models.IntegerField(default="0")
    image = models.ImageField(default='default.jpg', upload_to='product_pics')

    def __str__(self):
        return self.name
