from django.shortcuts import render
from shopping_cart.models import Order
from products.models import Product
from django.views.generic import DetailView


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


def product_list(request):
    objects_list = Product.objects.all()
    current_order_products = []

    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(owner=request.user.account, is_ordered=False)

        if filtered_orders:
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

    context = {
        'products': objects_list,
        'current_order_products': current_order_products }

    return render(request, 'products/product_list.html', context)
