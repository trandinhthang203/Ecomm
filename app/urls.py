from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('detail/', views.detail, name="detail"),
    path('list/', views.product_list,name="product_list"),
    path('create/', views.product_create,name="product_create"),
    path('update/<int:id>/', views.product_update,name="product_update"),
    path('delete/<int:id>/', views.product_delete,name="product_delete")
]
