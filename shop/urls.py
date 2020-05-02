from django.urls import path
from shop import views

app_name='shop'

urlpatterns = [

    path("",views.home,name='home'),
    path("dresses/",views.dresses,name='dresses'),
    path("sarees/",views.sarees,name='sarees'),
    path("lehangas/",views.lehangas,name='lehangas'),
    path(r'^(?P<category_slug>[-\w]+)/$', views.dresses, name='dresses'),
    path(r'^(?P<category_slug>[-\w]+)/$', views.sarees, name='sarees'),
    path(r'^(?P<category_slug>[-\w]+)/$', views.lehangas, name='lehangas'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path("signup/",views.Signup,name="signup"),
    path("login/",views.login,name="login"),
    path("logout/", views.Logout,name="logout"),
    
    ]
