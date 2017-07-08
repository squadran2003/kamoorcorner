from django.contrib import admin

# Register your models here.
from .models import Order,OrderDetail,ConfirmedOrder

class OrderDetailInline(admin.StackedInline):
    model = OrderDetail


class ConfirmOrderInline(admin.StackedInline):
    model = ConfirmedOrder

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline,ConfirmOrderInline]
    labels = {'pk':'Order no',}
    list_display = ('pk','created_on','confirmed','dispatched')
    search_fields = ('confirmed','dispatched')



admin.site.register(Order,OrderAdmin)
