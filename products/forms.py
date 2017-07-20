from django import forms

from .models import  Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    hidden = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model=Product
        fields=['title','description','Cost','image']

    def clean(self):
        data = self.cleaned_data
        if data['hidden'] !='':
            raise ValidationError('Must not be entered by bots')
        return data
