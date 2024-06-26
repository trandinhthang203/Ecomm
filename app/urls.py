from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('delete/<int:id>/', views.product_delete,name="product_delete"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('account_list/', views.account_list,name="account_list"),
    path('accounts/update/<int:id>/', views.account_update, name='account_update'),
    path('account_create/', views.account_create,name="account_create"),
    path('check-username/', views.check_username, name='check_username'),
    path('check-email/', views.check_email, name='check_email'),
    path('check-name/', views.check_name, name='check_name'),
    path('check-phone/', views.check_phone, name='check_phone'),
]
urlpatterns += static(settings.MEDIA_URL   , document_root=settings.MEDIA_ROOT)