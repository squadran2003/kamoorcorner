from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^order/view_cart/$', views.view_cart,name='view_cart'),
    url(r'^order/add_to_cart/(?P<product_id>[0-9]+)/$', views.add_to_cart,name='add_to_cart'),
    url(r'^order/remove_from_cart/(?P<product_id>[0-9]+)/$', views.remove_from_cart,name='remove_from_cart'),
    url(r'^order/confirm_order/(?P<user_id>\d+)/(?P<order_no>\d+)/(?P<confirmed>\w+)/$', views.confirm_order,name='confirm_order'),
    url(r'^order/new_order/$', views.new_order,name='new_order'),
    url(r'^(?P<pk>\d+)/$', views.order_detail,name='order_detail'),
    url(r'^$', views.orders,name='all_orders'),

]
