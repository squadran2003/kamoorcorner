from django.contrib import admin

# Register your models here.

from .models import Product
from .forms import ProductForm

class Product_admin(admin.ModelAdmin):
    form = ProductForm

admin.site.register(Product,Product_admin)
