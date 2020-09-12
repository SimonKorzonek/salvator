from django.shortcuts import render, get_object_or_404, redirect
from .extras import get_user_pending_order
from users.models import Account
from products.models import Product
from shopping_cart.models import Order, OrderItem
from .extras import generate_order_id
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from datetime import datetime
from .forms import DeliveryForm
from products.forms import ProductQuantityForm


@login_required()
def shopping_cart(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order }
    return render(request, 'shopping_cart/shopping_cart.html', context)


@login_required()
def delivery(request):
    existing_order = get_user_pending_order(request)

    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=existing_order)

        if form.is_valid():
            Order.delivery_option = form.cleaned_data['delivery_option']
            Order.address = form.cleaned_data['address']
            Order.postcode = form.cleaned_data['postcode']
            Order.city = form.cleaned_data['postcode']
            Order.phone_number = form.cleaned_data['phone_number']
            form.save()
            return redirect('checkout')
    else:
        form = DeliveryForm(instance=existing_order)

    context = {
        'order': existing_order,
        'form': form }

    return render(request, 'shopping_cart/delivery.html', context)


@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Account, user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()

    order_item, was_created = OrderItem.objects.get_or_create(product=product)
    user_order, was_created = Order.objects.get_or_create(owner=user_profile, is_ordered=False)

    user_order.items.add(order_item)

    if was_created:
        user_order.ref_code = generate_order_id()
        user_order.save()

    messages.info(request, "item added to cart")
    return redirect(reverse('product_list'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart'))


@login_required()
def checkout(request, **kwargs):
    existing_order = get_user_pending_order(request)

    context = {
        'order': existing_order}

    return render(request, 'shopping_cart/checkout.html', context)


@login_required()
def update_transaction_records(request, token):
    # get the order being processed
    order_to_purchase = get_user_pending_order(request)

    # update the placed order
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
    order_to_purchase.save()
    
    # get all items in the order - generates a queryset
    order_items = order_to_purchase.items.all()

    # update order items
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    # Add products to user profile
    user_profile = get_object_or_404(Account, user=request.user)
    # get the products from the items
    order_products = [item.product for item in order_items]
    user_profile.ebooks.add(*order_products)
    user_profile.save()
    messages.info(request, 'thank you')
    return redirect(reverse('accounts:my_profile'))


def success(request, **kwargs):
    return render(request, 'shoping_cart/purchase_success.html', {})