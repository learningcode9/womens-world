from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url('order_create/', views.order_create, name='order_create')
]