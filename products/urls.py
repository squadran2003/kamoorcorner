from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'products/$', views.products,name='products'),
    url(r'products/(?P<pk>\d+)/$', views.product_detail,name='product_detail'),

]
