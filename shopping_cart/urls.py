from django.urls import path
from . import views


urlpatterns = [
    path('', views.shopping_cart, name='shopping_cart'),
    path('add-to-cart/<int:item_id>', views.add_to_cart, name='add_to_cart'),
    path('success/', views.success, name='purchase_success'),
    path('item/delete/<int:item_id>', views.delete_from_cart, name='delete_item'),
    path('delivery', views.delivery, name='delivery'),
    path('checkout/', views.checkout, name='checkout'),
    path('update-transaction/<token>', views.update_transaction_records, name='update_records')
]
