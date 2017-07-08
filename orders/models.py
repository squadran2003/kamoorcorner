from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User)
    total_cost = models.DecimalField(max_digits = 20,decimal_places = 2,default=0.00)
    confirmed = models.BooleanField(default=False)
    dispatched = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return 'Order No {}'.format(self.pk)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']


class ConfirmedOrder(models.Model):
    order = models.ForeignKey(Order)
    user = models.ForeignKey(User)
    address = models.TextField()
    phone_number = PhoneNumberField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
