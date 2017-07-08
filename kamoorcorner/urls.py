"""kamurcorner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from . import views
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^orders/',include('orders.urls',namespace='orders')),
    url(r'^kamoor_korner_accounts/',include('kkaccounts.urls',namespace='kkaccounts')),
    url(r'^accounts/',include('django.contrib.auth.urls',namespace='accounts')),
    url(r'^accounts/password_reset/done/$',auth_views.password_reset_done,{'template_name':
                                                            'registration/password_reset_done.html'},
                                                            name='password_reset_done'),
    url(r'^accounts/password_reset/complete/$',auth_views.password_reset_complete,{'template_name':
                                                                'registration/password_reset_complete.html'},
                                                                name='password_reset_complete'),
    url(r'^$',views.home,name='home'),

]

urlpatterns+=staticfiles_urlpatterns()
