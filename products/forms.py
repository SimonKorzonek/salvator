from django import forms
from shopping_cart.models import OrderItem

class ProductQuantityForm(forms.ModelForm):
    quantity = forms.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['quantity']