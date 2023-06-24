from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    model = Order
    exclude = []
    widgets = {
        'size' : forms.RadioSelect
    }