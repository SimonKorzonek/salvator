from django import forms
from .models import Order
from multiselectfield import MultiSelectField

DELIVERY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'))

class DeliveryForm(forms.ModelForm):
    delivery_option = MultiSelectField(choices=DELIVERY_CHOICES, max_choices=1)
    address = forms.CharField(required=True, max_length=120)
    postcode = forms.CharField(required=True, max_length=6)
    city = forms.CharField(required=True, max_length=30)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = Order
        fields = ['delivery_option', 'address', 'postcode', 'city', 'phone_number']
