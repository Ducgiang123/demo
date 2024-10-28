"""
URL configuration for htqlbh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=False)),  
    path('home/', views.home, name='home'),  
] + [
    path('product/', views.product, name='product'),
    path('create_product/', views.create_product, name='create_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('search_product/', views.search_product, name='search_product'),
]+[
    path('customer/', views.customer, name='customer'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('update_customer/', views.update_customer, name='update_customer'),
    path('delete_customer/', views.delete_customer, name='delete_customer'),
    path('search_customer/', views.search_customer, name='search_customer'),
]+[
    path('invoice/', views.invoice, name='invoice'),
    path('get_invoice_id_create/', views.get_invoice_id_create, name='get_invoice_id_create'),
    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('save_create_invoice/', views.save_create_invoice, name='save_create_invoice'),
    path('create_invoice_detail/', views.create_invoice_detail, name='create_invoice_detail'),
    path('load_data_create_invoice_detail/', views.load_data_create_invoice_detail, name='load_data_create_invoice_detail'),
    path('delete_invoice_detail/', views.delete_invoice_detail, name='delete_invoice_detail'),
    path('get_total_cost_create_invoice/', views.get_total_cost_create_invoice, name='get_total_cost_create_invoice'),
    path('update_invoice/', views.update_invoice, name='update_invoice'),
    path('update_invoice_detail/', views.update_invoice_detail, name='update_invoice_detail'),
    path('load_data_update_invoice_detail/', views.load_data_update_invoice_detail, name='load_data_update_invoice_detail'),
    path('get_total_cost_update_invoice/', views.get_total_cost_update_invoice, name='get_total_cost_update_invoice'),
    path('search_invoice/', views.search_invoice, name='search_invoice'),
    path('load_data_view_invoice_detail/', views.load_data_view_invoice_detail, name='load_data_view_invoice_detail'),
    path('get_customer_list/', views.get_customer_list, name='get_customer_list'),
    path('get_product_list/', views.get_product_list, name='get_product_list'),
] + [
    path('statistics/', views.statistics, name='statistics'),
    path('sales_revenue/', views.sales_revenue, name='sales_revenue'),
]
