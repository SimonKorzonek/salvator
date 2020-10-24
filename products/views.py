from shopping_cart.models import Order
from products.models import Product
from django.views.generic import DetailView, ListView
from .forms import ProductSearchForm


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        form = ProductSearchForm(self.request.GET)
        current_order_products = []

        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            sort_by = form.cleaned_data['sort_by']
            per_page = form.cleaned_data['per_page']

            if per_page:
                self.request.session['per_page'] = per_page

            if name:
                queryset = queryset.filter(name__icontains=name)


            #  C A T E G O R Y
            if not category:
                try:
                    if not queryset.filter(category=self.request.session['category']):
                        queryset = queryset
                    else:
                        queryset = queryset.filter(category=self.request.session['category'])
                except:
                    pass
            elif category.name == 'all':
                self.request.session['category'] = category.id
                queryset = queryset
            else:
                self.request.session['category'] = category.id
                queryset = queryset.filter(category=category)



            #  S O R T I N G
            if sort_by:
                self.request.session['sort_by'] = sort_by
                if sort_by == 'price ascending':
                    queryset = queryset.order_by('price')
                elif sort_by == 'price descending':
                    queryset = queryset.order_by('-price')
            else:
                try:
                    if self.request.session['sort_by'] == 'price ascending':
                        queryset = queryset.order_by('price')
                    elif self.request.session['sort_by'] == 'price descending':
                        queryset = queryset.order_by('-price')
                except:
                    pass


        if self.request.user.is_authenticated:
            filtered_orders = Order.objects.filter(owner=self.request.user.account, is_ordered=False)
            if filtered_orders:
                user_order = filtered_orders[0]
                user_order_items = user_order.items.all()
                current_order_products = [product.product for product in user_order_items]


        return super().get_context_data(
            form=form,
            object_list=queryset,
            current_order_products=current_order_products,
            **kwargs)


    def get_paginate_by(self, queryset):
        try:
            return self.request.session['per_page']
        except:
            return 3  # default paginate_by
