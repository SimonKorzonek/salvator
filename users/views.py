from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, AccountUpdateForm
from .models import Account
from shopping_cart.models import Order


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created, {username}! Now you're able to log in!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def account(request):
    return render(request, 'users/account.html')


@login_required
def update_account(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        account_update_form = AccountUpdateForm(request.POST, instance=request.user.account)

        if user_update_form.is_valid() and account_update_form.is_valid():
            user_update_form.save()
            account_update_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('account')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        account_update_form = AccountUpdateForm(instance=request.user.account)

    context = {
        'user_update_form': user_update_form,
        'account_update_form': account_update_form
        }

    return render(request, 'users/update_account.html', context)

#my_profile in tutorial
@login_required
def orders(request):
    ordering_account = Account.objects.filter(user=request.user).first()
    account_orders = Order.objects.filter(is_ordered=True, owner=ordering_account)
    context = {
        'account_orders': account_orders}
    return render(request, 'users/orders.html', context)