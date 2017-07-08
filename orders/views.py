from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# Create your views here.
from products.models import Product
from cart.cart import *
from .models import Order
from .forms import OrderForm,OrderDetailForm,ConfirmOrderForm


def orders(request):
    orders = Order.objects.filter(confirmed=True)
    return render(request,'orders/orders.html',{'orders':orders})

def order_detail(request,pk):
    order = get_object_or_404(Order,pk=pk)
    return render(request,'orders/order_detail.html',{'order':order})


@login_required
def new_order(request):
    old_cart_products = []
    cart = Cart(request)
    form1= OrderForm(request.POST or None)
    form2 = OrderDetailForm(request.POST or None)
    order_instance = form1.save(commit=False)
    try:
        shopping_cost = shopping_cart_total(cart)
        order_instance.user = request.user
        order_instance.total_cost = shopping_cost
        order_instance.save()
        for item in cart:
            order_detail_instance = form2.save(commit=False)
            order_detail_instance.pk = None
            order_detail_instance.order = order_instance
            order_detail_instance.product = item.product
            order_detail_instance.quantity = item.quantity
            order_detail_instance.save()
            old_cart_products.append(item.product)

        # send email
        subject = 'Your order from kamoor korner'
        sender = "noreply@kamoorkorner.com"
        receiver = [request.user.email,]
        context = {'cart':cart,'total_cost':shopping_cost,
                    'username':request.user.username,
        'link':'http://www.kamoorkorner/com/orders/order/confirm_order/{}/{}/True/'.format(request.user.id,order_instance.pk)}
        send_new_order_mail (subject,sender,receiver,context)
        #remove products from the cart once the order has been placed

        remove_old_products_from_cart(cart,old_cart_products)
        messages.success(request,'We have sent you an email,'
                                ' please click on the link to confirm order!')
    except Exception as e:
        messages.warning(request,'Error placing order: {}'.format(e))
    return redirect('home')


def confirm_order(request,user_id,order_no,confirmed):
    form = ConfirmOrderForm(request.POST or None)
    # confirm the order
    order = get_object_or_404(Order,pk=order_no)
    #check to see if the order is confirmed
    order.confirmed = confirmed
    order.save()
    user = User.objects.get(pk=user_id)
    if request.method=='POST':
        form = ConfirmOrderForm(request.POST or None)
        if not order.confirmed:
            if form.is_valid():
                try:
                    instance = form.save(commit=False)
                    instance.order = order
                    instance.user = user
                    instance.address = form.cleaned_data['address']
                    instance.phone_number = form.cleaned_data['phone_number']
                    instance.save()
                    subject = 'New order placed at kamoor korner'
                    sender = "noreply@kamoorkorner.com"
                    receiver = ['kamoorkorner@gmail.com',]
                    context = {'order':order,'username':request.user.username}
                    send_confirmation_order_mail(subject,sender,receiver,context)
                    messages.success(request,'Your order has been confirmed,'
                                                ' we will contact you shortly')
                except Exception as e:
                    messages.warning(request,'Error confirming order: {}'.format(e))
            return redirect('home')
        else:
            messages.warning(request,'That order has already been confirmed!')
            return redirect('orders:confirm_order',user_id=user_id,order_no=order_no,confirmed=confirmed)
    return render(request,'orders/confirm_order.html',{'form':form})


@login_required
def add_to_cart(request,product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart(request)
    cost = product.Cost
    if request.method=='POST':
        form = OrderDetailForm(request.POST or None)
        if form.is_valid():
            try:
                quantity = form.cleaned_data['quantity']
                cart.add(product,product.Cost,quantity)
                messages.success(request,'Your item has been added to the cart!')
            except:
                messages.warning(request,'Error adding item to cart!')
    return redirect('home')

@login_required
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    total_cost = 0
    count = 0
    for item in cart:
        count+=1
        total_cost+=item.total_price
    try:
        cart.remove(product)
        messages.success(request,'Your item has been removed from the cart!')
    except:
        messages.error(request,'Error removing item from cart!')
    if count < 2:
        return redirect('home')
    else:
        return render(request,'orders/cart.html',{'cart':cart,
                                            'total_cost':total_cost})

@login_required
def view_cart(request):
    cart = Cart(request)
    total_cost = shopping_cart_total(cart)
    count = 0
    for item in cart:
        count +=1
    if count < 1:
        messages.success(request,'No items in your cart yet!')
        return redirect('home')
    return render(request,'orders/cart.html',{'cart':cart,
                                                'total_cost':total_cost,
                                                })

def shopping_cart_total(cart):
    total = 0
    for item in cart:
        total+=item.total_price
    return total


def remove_old_products_from_cart(cart,old_products):
    for item in old_products:
        cart.remove(item)


def send_new_order_mail(subject,sender,receiver,context):
    plain_text = get_template('emails/new_order.txt')
    htmly = get_template('emails/new_order.html')
    text_content = plain_text.render()
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(subject,text_content,sender,receiver)
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def send_confirmation_order_mail(subject,sender,receiver,context):
    plain_text = get_template('emails/confirm_order.txt')
    htmly = get_template('emails/confirmation_email.html')
    text_content = plain_text.render()
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(subject,text_content,sender,receiver)
    msg.attach_alternative(html_content,'text/html')
    msg.send()
