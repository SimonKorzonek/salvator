from django import forms
from shopping_cart.models import OrderItem
from products.models import Product

class ProductQuantityForm(forms.ModelForm):
    quantity = forms.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['quantity']



class ProductSearchForm(forms.ModelForm):
    SORTING = ('price ascending', 'price descending')
    AMOUNT = ('1', '2', '3', '5', '10')
    sort_by = forms.ChoiceField(choices=[('', '')] + list(zip(SORTING, SORTING)))
    per_page = forms.ChoiceField(choices=[('', '')] + list(zip(AMOUNT, AMOUNT)))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False

    class Meta:
        model = Product
        fields = ('name', 'category', 'sort_by', 'per_page')
