from django import forms

from .models import  Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model:Product
