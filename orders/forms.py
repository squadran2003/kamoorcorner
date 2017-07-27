from django.forms import ModelForm
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Order,OrderDetail,ConfirmedOrder

class OrderForm(ModelForm):
    hidden = forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Order
        fields = ['id']

    def clean(self):
        data = self.cleaned_data
        if data['hidden'] !='':
            raise ValidationError('Must not be entered by bots')
        return data


class OrderDetailForm(ModelForm):
    hidden = forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = OrderDetail
        fields = ['quantity']

    def clean(self):
        data = self.cleaned_data
        if data['hidden'] !='':
            raise ValidationError('Must not be entered by bots')
        return data


class ConfirmOrderForm(ModelForm):
    hidden = forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = ConfirmedOrder
        fields = ['address','phone_number']
        help_texts = {
            'phone_number': ('Enter phone number including country code!'),
        }

    def clean(self):
        data = self.cleaned_data
        address = data['address']
        if address == '':
            raise ValidationError('Address cannot be blank')
        elif data['hidden']!='':
            raise ValidationError('Must not be entered by bots')
        return data
