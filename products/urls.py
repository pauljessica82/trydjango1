from django.contrib import admin
from django.urls import path

from products.views import (
    ProductCreateView,
    ProductDetailView,
    ProductDeleteView,
    ProductUpdateView,
    ProductListView

)

app_name = 'products'
urlpatterns = [

    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:id>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:id>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('', ProductListView.as_view(), name='product-list')

]
