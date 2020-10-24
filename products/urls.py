from django.urls import path
from .views import ProductDetailView, ProductListView
# from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail')  # expects int variable. PK comes from primary key of product
]
