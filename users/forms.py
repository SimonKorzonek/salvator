from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class AccountUpdateForm(forms.ModelForm):
    address = forms.CharField(required=False)
    postcode = forms.CharField(required=False)
    city = forms.CharField(max_length=30, required=False)
    payment_method = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Account
        fields = ['address', 'postcode', 'city', 'payment_method']
        labels = {'address': 'Address'}