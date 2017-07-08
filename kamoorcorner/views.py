from django.shortcuts import render
from products.models import Product
from orders.forms import OrderDetailForm
from orders.models import Order
from cart.cart import *

def home(request):
    products = Product.objects.all()
    # get the items in the cart
    cart = Cart(request)
    # get all the confirmed orders
    orders = Order.objects.filter(confirmed=True)
    form = OrderDetailForm()
    # dividing the column with by products so i know how much width to apply
    #to the bootstrap grid
    product_count = len(products)
    if(product_count==1):
        col_class ='col-sm-12'

    elif(product_count==2):
        col_class='col-sm-6'
    else:
        col_class='col-sm-4'

    return render(request,'home.html',{'products':products,
                                        'form':form,'cart':cart,
                                        'col_class':col_class,
                                        'orders':orders})
