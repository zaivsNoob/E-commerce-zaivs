
from .models import ShippingAdress,Order
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ShippingForm(forms.ModelForm):

    
    def __init__(self, user, order_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['customer'].choices = [(user.customer.id, user.customer)]
        self.fields['order'].choices = [(order_id, Order.objects.get(id=order_id))]
       
    class Meta:
        model = ShippingAdress
        fields = ['customer', 'order', 'address']
        widgets = {
            'customer': forms.HiddenInput(),
            'order': forms.HiddenInput(),
        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
