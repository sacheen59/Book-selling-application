from django import forms
from .models import Order

class OrderFrom(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity','address','contact_no','payment_method']