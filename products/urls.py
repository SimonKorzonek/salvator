from django.urls import path
from .views import ProductDetailView
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')  # expects int variable. PK comes from peimart key of product, field automaticly added by django models
]
