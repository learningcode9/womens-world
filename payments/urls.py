from django.conf.urls import url
from .import views
app_name='payments'

urlpatterns=[
    url('process',views.payment_process,name='process'),
    url('done',views.payment_done,name='done'),
    url('canceled',views.payment_canceled,name='canceled'),
]