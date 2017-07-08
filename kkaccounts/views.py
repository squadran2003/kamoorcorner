from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout
from django.views import generic

from . import forms

# Create your views here.

class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = "kkaccounts/signup.html"
