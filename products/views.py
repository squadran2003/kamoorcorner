from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages

# Create your views here.
from . import models
from .forms import ProductForm

def products(request):
    products = models.Product.objects.all()
    return render(request,'products/products.html',{'products':products})


def product_detail(request,pk):
    product = get_object_or_404(models.Product,pk=pk)
    form = ProductForm(instance=product)
    if request.method=='POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Product has been updated!')
            except Exception as e:
                messages.warning(request,'Error updating product! {}'.format(e))
        return render(request,'products/product_detail.html',{'product':product,'form':form})
    return render(request,'products/product_detail.html',{'product':product,'form':form})
